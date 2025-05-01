from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.contrib.admin.models import ADDITION, CHANGE, DELETION
from django_auditlog.mixin import AuditLoggerMixin


@receiver(pre_save)
@receiver(pre_delete)
def store_original_pre_save(sender, instance, **kwargs):
    if isinstance(instance, AuditLoggerMixin):
        instance.store_original()


@receiver(post_save)
def auto_log_save(sender, instance, created, **kwargs):
    if not issubclass(sender, AuditLoggerMixin):
        return
    if created:
        instance.log_change(ADDITION, "Auto-created")
    else:
        if hasattr(instance, "_original_values"):
            diffs = instance.get_field_diff()
            msg = "; ".join(f"{k}: {v['from']} → {v['to']}" for k, v in diffs.items())
        else:
            msg = "Auto-updated"
        instance.log_change(CHANGE, msg)


@receiver(post_delete)
def auto_log_delete(sender, instance, **kwargs):
    if not issubclass(sender, AuditLoggerMixin):
        return
    snapshot = {f.name: getattr(instance, f.name) for f in instance._meta.fields}
    instance.log_change(DELETION, f"Deleted: {snapshot}")

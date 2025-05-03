from django.db import models
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django_auditlog.middleware import get_current_request


class AuditLoggerMixin(models.Model):
    class Meta:
        abstract = True

    def store_original(self):
        instance = self._meta.model.objects.filter(pk=self.pk).first()
        if instance is not None:
            self._original_values = {
                field.name: getattr(instance, field.name) for field in self._meta.fields
            }

    def get_field_diff(self):
        diffs = {}
        for field in self._meta.fields:
            name = field.name
            old = self._original_values.get(name)
            new = getattr(self, name)
            if old != new:
                diffs[name] = {"from": old, "to": new}
        return diffs

    def log_change(self, action_flag, change_message=""):
        request = get_current_request()
        if (
            not request
            or not hasattr(request, "user")
            or not request.user.is_authenticated
        ):
            return
        LogEntry.objects.log_action(
            user_id=request.user.id,
            content_type_id=ContentType.objects.get_for_model(self).pk,
            object_id=str(self.pk),
            object_repr=str(self),
            action_flag=action_flag,
            change_message=change_message,
        )

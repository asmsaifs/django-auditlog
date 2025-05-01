from django.apps import AppConfig


class DjangoAuditlogConfig(AppConfig):
    name = "django_auditlog"

    def ready(self):
        import django_auditlog.signals

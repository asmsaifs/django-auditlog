# django_auditlog

Django mixin for automatic create/update/delete audit logging using Django's built-in `LogEntry`.

## Features

- Per-field change tracking
- No extra tables (uses admin.LogEntry)
- Works with DRF or custom logic
- Middleware-based user detection

## Installation

```bash
pip install django_auditlog
```

## Usage

```python
from django_auditlog.mixin import AuditLoggerMixin

class Book(AuditLoggerMixin, models.Model):
    ...
```

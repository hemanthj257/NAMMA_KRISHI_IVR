from django.db import models

class CallLog(models.Model):
    call_sid = models.CharField(max_length=64, unique=True)
    from_number = models.CharField(max_length=20)
    to_number = models.CharField(max_length=20)
    status = models.CharField(max_length=32)
    duration = models.CharField(max_length=16, null=True, blank=True)
    direction = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Call from {self.from_number} to {self.to_number} - {self.status}"

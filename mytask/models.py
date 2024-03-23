# myapp/models.py
from django.db import models

class TaskResult(models.Model):
    result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result: {self.result}, Created At: {self.created_at}"

from django.contrib.auth.models import User
from django.db import models

NOT_COMPLETED = 0
NOT_COMPLETED_ADMIN_EDIT = 1
FULLY_COMPLETED = 10
FULLY_COMPLETED_ADMIN_EDIT = 11
STATUS_CHOICE = (
    (NOT_COMPLETED, 'NOT_COMPLETED'),
    (NOT_COMPLETED_ADMIN_EDIT, 'NOT_COMPLETED_ADMIN_EDIT'),
    (FULLY_COMPLETED, 'FULLY_COMPLETED'),
    (FULLY_COMPLETED_ADMIN_EDIT, 'FULLY_COMPLETED_ADMIN_EDIT'),
)


class TodoText(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    text = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICE, verbose_name="status_completed")

    def __str__(self):
        return self.username

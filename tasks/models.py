from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Complete'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    deadline = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-title']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
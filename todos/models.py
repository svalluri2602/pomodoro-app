from django.db import models
from pomodoro_sessions.models import Session

# Create your models here.

class Todo(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name = 'todos')
    text = models.CharField(max_length = 300)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text

        

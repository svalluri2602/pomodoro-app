from django.db import models
from projects.models import Project

class Session(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"Session for {self.project.name} at {self.start_time}"

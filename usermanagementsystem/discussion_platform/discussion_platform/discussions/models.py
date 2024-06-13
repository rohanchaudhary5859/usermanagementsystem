# discussion_platform/discussions/models.py

from django.db import models

class Discussion(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='discussion_images/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Discussion {self.id}"

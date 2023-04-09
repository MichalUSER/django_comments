from django.db import models
from django.utils import timezone


class Comment(models.Model):
    content = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.content

    def is_today(self):
        return self.date.date() == timezone.localdate()

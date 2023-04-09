from django.db import models

class Comment(models.Model):
    content = models.CharField(max_length=50)
    date = models.DateTimeField()
    def __str__(self):
        return self.content

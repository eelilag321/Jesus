from django.db import models
from django.utils import timezone

class Prayer(models.Model) :
    name = models.CharField(max_length=100, default="")
    content = models.TextField(default="")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

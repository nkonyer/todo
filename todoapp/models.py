from django.db import models

# Create your models here.
from django.db import models


class TodoListItem(models.Model):
    content = models.TextField()
    isCompleted = models.BooleanField(default=False)
    beingEdited = models.BooleanField(default=False)
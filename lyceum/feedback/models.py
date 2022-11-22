from datetime import datetime

from django.db import models


class Feedback(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(default=datetime.now())

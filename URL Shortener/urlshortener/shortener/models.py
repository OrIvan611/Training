from django.db import models


class Url(models.Model):
    original_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=10, unique=True)
    counter = models.PositiveSmallIntegerField(default=0)


from django.db import models


class Study(models.Model):
  name = models.CharField(max_length=255)

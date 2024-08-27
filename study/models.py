from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Study(models.Model):
  name = models.CharField(
    max_length=255,
    verbose_name="Study Name",
    help_text="Enter the name of the study",
  )

  description = models.TextField(
    verbose_name="Description",
    help_text="Enter the description of the study",
    null=True,
  )

  number_of_places = models.IntegerField(
    verbose_name="Number of Places",
    help_text="Enter the number of places in the study",
    validators=[
      MinValueValidator(1),
      MaxValueValidator(5000),
    ],
    default=1,
  )

  reward = models.IntegerField(
    verbose_name="Reward",
    help_text="Enter the reward for participating in the study",
    validators=[
      MinValueValidator(10),
      MaxValueValidator(10000),
    ],
    default=10,
  )

  creator = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    verbose_name="Creator",
    help_text="Enter the creator of the study",
  )

  def __str__(self):
    return self.name

# Generated by Django 5.1 on 2024-08-27 15:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_study_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='estimated_time_minutes',
            field=models.IntegerField(default=5, help_text='Enter the estimated time in minutes to complete the study', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(60)], verbose_name='Estimated Time in Minutes'),
            preserve_default=False,
        ),
    ]

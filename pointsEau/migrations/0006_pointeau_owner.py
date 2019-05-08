# Generated by Django 2.2.1 on 2019-05-08 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pointsEau', '0005_pointeau_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointeau',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

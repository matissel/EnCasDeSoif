# Generated by Django 2.2.1 on 2019-05-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointsEau', '0002_pointeau_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointeau',
            name='description',
            field=models.CharField(default='Description', max_length=255),
        ),
    ]
# Generated by Django 5.0 on 2023-12-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicianmodel',
            name='instrument_type',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
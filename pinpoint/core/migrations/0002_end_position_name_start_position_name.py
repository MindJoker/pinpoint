# Generated by Django 5.0.3 on 2024-03-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='end',
            name='position_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='start',
            name='position_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

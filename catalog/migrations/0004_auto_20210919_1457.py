# Generated by Django 3.1.7 on 2021-09-19 11:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210919_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='id',
            field=models.UUIDField(default=uuid.UUID('242fe214-e7a2-4cf8-bfcc-e9106b1f5e90'), help_text='ID случая', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(default=1, help_text='ID пациента', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='visit',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7c79fbef-d3b8-421c-995f-f49b6820ce89'), help_text='ID посещения', primary_key=True, serialize=False),
        ),
    ]

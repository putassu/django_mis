# Generated by Django 3.1.7 on 2021-09-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20210913_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcd',
            name='code',
            field=models.CharField(default='1', help_text='Код болезни', max_length=20),
        ),
    ]

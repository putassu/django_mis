# Generated by Django 3.1.7 on 2021-09-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20210913_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='diagnosis',
        ),
        migrations.AlterField(
            model_name='case',
            name='id',
            field=models.AutoField(help_text='ID случая', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='case',
            name='reason',
            field=models.CharField(blank=True, choices=[('1', 'Лечебно-диагностический прием '), ('2', 'Консультативный прием '), ('3', 'Диспансерное наблюдение '), ('4', 'Профилактический прием'), ('5', 'Профессиональный осмотр'), ('6', 'Реабилитационный прием'), ('7', 'Зубопротезный прием'), ('8', 'Протезно-ортопедический прием'), ('9', 'Обращение в центр здоровья'), ('10', 'Дополнительная диспансеризация'), ('11', 'Патронаж'), ('12', 'Другие')], help_text='Повод обращения', max_length=2, verbose_name='Повод обращения'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(help_text='ID пациента', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patronym',
            field=models.CharField(blank=True, max_length=25, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='id',
            field=models.AutoField(help_text='ID посещения', primary_key=True, serialize=False),
        ),
    ]
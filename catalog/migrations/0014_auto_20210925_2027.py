# Generated by Django 3.1.7 on 2021-09-25 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0013_auto_20210919_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='doctor',
            field=models.ForeignKey(help_text='Врач', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Врач'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_10_00',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='10:00'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_10_20',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='10:20'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_10_40',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='10:40'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_11_00',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='11:00'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_11_20',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='11:20'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_11_40',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='11:40'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_13_00',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='13:00'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_13_20',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='13:20'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_13_40',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='13:40'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_14_00',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='14:00'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_14_20',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='14:20'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_14_40',
            field=models.CharField(choices=[('Андрей Васильев (1998-09-19) г.р.', 'Андрей Васильев (1998-09-19) г.р.'), ('Лев Тигров (2000-09-19) г.р.', 'Лев Тигров (2000-09-19) г.р.'), ('Лев Тигров2 (2000-09-19) г.р.', 'Лев Тигров2 (2000-09-19) г.р.'), ('Персона нон (1996-09-25) г.р.', 'Персона нон (1996-09-25) г.р.'), ('Нет записи', 'Нет записи')], default='Нет записи', max_length=50, null=True, verbose_name='14:40'),
        ),
    ]

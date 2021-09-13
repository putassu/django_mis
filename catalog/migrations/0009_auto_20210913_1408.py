# Generated by Django 3.1.7 on 2021-09-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20210512_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название болезни', max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='case',
            options={'ordering': ['date'], 'verbose_name': 'случай', 'verbose_name_plural': 'Случаи'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['last_name'], 'verbose_name': 'пациента', 'verbose_name_plural': 'Пациенты'},
        ),
        migrations.AlterModelOptions(
            name='visit',
            options={'ordering': ['date'], 'verbose_name': 'посещение', 'verbose_name_plural': 'Посещения'},
        ),
        migrations.AddField(
            model_name='case',
            name='diagnosis',
            field=models.ManyToManyField(help_text='Выберите диагноз', to='catalog.MCD'),
        ),
    ]

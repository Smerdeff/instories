# Generated by Django 2.2.13 on 2020-06-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название опции')),
                ('value', models.BooleanField(verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Опция',
                'verbose_name_plural': 'Опции',
            },
        ),
        migrations.CreateModel(
            name='Pushes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок уведомления')),
                ('text', models.TextField(verbose_name='Текст уведомлния')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_at', models.DateField(verbose_name='Дата отправки')),
                ('is_sent', models.BooleanField(default=False, verbose_name='Отправлен')),
            ],
            options={
                'verbose_name': 'Пуш уведомление',
                'verbose_name_plural': 'Пуш уведомления',
            },
        ),
    ]

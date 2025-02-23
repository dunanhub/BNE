# Generated by Django 4.2.16 on 2024-11-25 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50, verbose_name='Имя')),
                ('SurName', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('Number', models.CharField(max_length=20, verbose_name='Номер Телефона')),
                ('Age', models.IntegerField(verbose_name='Возраст')),
                ('NameClub', models.CharField(blank=True, max_length=50, verbose_name='Клуб')),
                ('NameNews', models.CharField(blank=True, max_length=50, verbose_name='Событие')),
                ('University', models.CharField(blank=True, max_length=50, verbose_name='Университет')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClubName', models.CharField(max_length=50, verbose_name='Название Клуба')),
                ('NewsName', models.CharField(max_length=50, verbose_name='Название Новости')),
                ('Anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('TextNews', models.TextField(verbose_name='Статья')),
                ('Date', models.DateTimeField(verbose_name='Дата события')),
                ('Date_Stop', models.DateTimeField(default=datetime.datetime.now, verbose_name='Закрытие регистрации')),
                ('ImgNews', models.ImageField(blank=True, upload_to='main/static/main/post/', verbose_name='Картинка Новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]

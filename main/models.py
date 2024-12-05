from django.db import models
from django.utils import timezone
from datetime import datetime
import os
# Create your models here.

class Post(models.Model): #Создаем модель (своего рода словарь) где ключи это переменные, а тип все что после равно это в каком формате мы принимем значения
    ClubName= models.CharField('Название Клуба',max_length=50)
    NewsName = models.CharField('Название Новости',max_length=50)
    Anons = models.CharField('Анонс',max_length=250)
    TextNews=models.TextField('Статья')
    Date = models.DateTimeField("Дата события")
    Date_Stop = models.DateTimeField("Закрытие регистрации", default=datetime.now)
    ImgNews =  models.ImageField("Картинка Новости", blank = True, upload_to='media')
    
    def __str__(self):
        return self.ClubName
    
    def delete(self, *args, **kwargs):
        # Удаляем файл изображения, если он существует
        if self.ImgNews:
            if os.path.isfile(self.ImgNews.path):
                os.remove(self.ImgNews.path)
        super().delete(*args, **kwargs)  # Вызываем стандартное удаление модели
        
    class Meta: #Создаем название таблицы в странице алминистратора для нашей модели
        verbose_name="Новость" #Единичсное число
        verbose_name_plural="Новости" #Множественное число
   

class Articles(models.Model): #Создаем модель (своего рода словарь) где ключи это переменные, а тип все что после равно это в каком формате мы принимем значения
    FirstName = models.CharField('Имя',max_length=50)
    SurName = models.CharField('Фамилия',max_length=50)
    Number = models.CharField('Номер Телефона',max_length=20)
    Age = models.IntegerField('Возраст')
    NameClub = models.CharField('Клуб',max_length=50,blank=True)
    NameNews = models.CharField('Событие',max_length=50,blank=True)
    University = models.CharField('Университет',max_length=50,blank=True)
    
    def __str__(self):
        return self.FirstName
    
    class Meta: 
        verbose_name="Участник" 
        verbose_name_plural="Участники" 
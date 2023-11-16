from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=250, verbose_name='ФИО', blank=True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'{self.title},{self.text}'


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.CharField(max_length=340, verbose_name="Описание")
    article = models.ManyToManyField(Article, verbose_name="Статья")

    def __str__(self):
        return f"{self.title},{self.article}"


class Team(models.Model):
    full_name = models.CharField(max_length=250, verbose_name='Имя с фамилией', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='team_members_img')
    city = models.CharField(max_length=250, verbose_name='Город', blank=True, null=True)
    country = models.CharField(max_length=250, verbose_name='Страна', blank=True, null=True)

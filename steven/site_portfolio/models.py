from pydoc import describe
from tabnanny import verbose
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

class Projects(models.Model):
    title = models.CharField('Название проекта', max_length=100)
    description = models.TextField('Описание проекта')
    image = models.CharField('Расположение изображения', max_length=100)
    
    def __str__(self):
        return  self.title

    class Meta:
        verbose_name ='Проект'
        verbose_name_plural = 'Проекты'
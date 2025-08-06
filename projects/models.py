from django.db import models
import datetime

class Technology(models.Model):
    name = models.CharField('Технология', max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Projects(models.Model):
    name = models.CharField('Имя Проекта', max_length=255)
    link = models.URLField('Ссылка')
    description = models.CharField('Описание', max_length=255, blank=True, default="")
    image = models.ImageField('Фотография', upload_to='projects/')
    year = models.DateField('Дата', null=True, blank=True)

    # здесь связь многие-ко-многим
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True)

    def __str__(self):
        return self.name
    
class skills(models.Model):
    name = models.CharField('Имя Скила', max_length=255)
    level = models.CharField('Уровень', max_length=255)
    link = models.URLField('Ссылка')
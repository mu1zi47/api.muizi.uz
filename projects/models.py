from django.db import models

class Projects(models.Model):
    name = models.CharField('Имя Проекта', max_length=255)
    link = models.URLField('Ссылка')
    image = models.ImageField('Фотография', upload_to='projects/')

    def __str__(self):
        return self.name
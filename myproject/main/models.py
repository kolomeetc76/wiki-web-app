from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')

    def get_absolute_url(self):
        return f"/{self.id}"
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задача'




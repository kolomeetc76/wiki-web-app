from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


#простейшая модель для создания записи, поле title не обязательно
class Task(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # title = models.CharField(max_length=50)
    task = models.TextField('Описание')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True) 
    
    


    def get_absolute_url(self):
        return reverse('category', kwargs={"pk": self.pk})


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задача'

    class MPTTMeta:
        order_insertion_by = ['name']


class User(): 
    pass
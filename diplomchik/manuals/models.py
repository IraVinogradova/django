from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


# создание таблицы в БД
class Type(models.Model):
    type = models.CharField(max_length=100,help_text='Введите тип продукта', verbose_name='Тип продукта')

    def __str__(self):
        return self.type   #

    class Meta:
        verbose_name = 'тип продукта'
        verbose_name_plural = 'Типы продукции'


class Companys(models.Model):
    name = models.CharField(max_length=30, help_text='введите имя компании',verbose_name='Имя компании')

    def __str__(self):
        return self.name   # Будет возвращатся имя

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Article(models.Model):
    objects = None
    descr = models.CharField(max_length=1000, help_text='Введите описание товара', verbose_name='Описание товара')

    name = models.CharField(max_length=30,  help_text='Введите имя продукта', verbose_name='Имя товара')
    price = models.IntegerField( help_text='Введите цену товара без скидки', verbose_name='Цена товара без скидки') # цена продукта
    company = models.ForeignKey(Companys, on_delete=models.CASCADE,  help_text='Введите компанию товара', verbose_name='Компания товара')   #Сылка на имя компании
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, help_text='Введите тип товара', verbose_name='Тип/типы товаров')
    cover = models.ImageField(verbose_name='Изображение')
    display = models.BooleanField(default=True)



    def __str__(self):
        return self.name   # Будет возвращатся имя

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'





class status(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,  help_text='Выберите товар', verbose_name='товар')
    due_back = models.DateField(help_text='Дата окончания статуса',verbose_name='Дата окончания статуса')

    def __str__(self):
        return self.due_back   # Будет возвращатся имя

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'



class Sum_of_article(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,  help_text='Выберите товар', verbose_name='товар')
    sum_of_article = models.IntegerField(help_text='Введите число товара', verbose_name='Количество товара')



    class Meta:
        verbose_name = 'Количество'
        verbose_name_plural = 'Количество'





class Skidka(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skidka = models.IntegerField(help_text='Размер скидки', verbose_name='Размер скидки')

    def __int__(self):
        return self.user   # Будет возвращатся имя

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'





from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    imagine = models.ImageField(upload_to='categorys/', verbose_name='Фотография', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    brand = models.CharField(max_length=100, verbose_name='Брэнд')
    description = models.TextField(verbose_name='Описание')
    imagine = models.ImageField(upload_to='books/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField()
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"Название: {self.title}. Автор: {self.brand}. Описание: {self.description}. " \
               f"Цена: {self.price}."

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

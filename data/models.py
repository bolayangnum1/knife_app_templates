from django.db import models
from django.core.validators import RegexValidator, DecimalValidator
from django.urls import reverse

from .notnecessary import parametersForNull


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"
        ordering = ('-name',)

    name = models.CharField('Название', max_length=100, validators=[
        RegexValidator(
            regex=r'\.$',
            message='уберите точку!',
            inverse_match=True,
        )
    ])
    image = models.ImageField('image')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', null=True, validators=[
        DecimalValidator(
            max_digits=8,
            decimal_places=2,
        )
    ])
    description = models.TextField('Описание')
    are_available = models.BooleanField('имеется в наличии', default=True)
    amount = models.IntegerField('Количество товара', blank=True, null=True)
    sale = models.IntegerField('Скидка в процентах', blank=True, default=0, null=True)
    url = models.SlugField(max_length=100)
    draft = models.BooleanField(default=False, verbose_name='Черновик')

    def __str__(self):
        return f'{self.name}'


class FotoProduct(models.Model):
    image = models.ImageField('Картинки товаров')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинки товаров'


class Recommendations(models.Model):
    name = models.CharField('Название', max_length=100)
    products = models.ManyToManyField(Product, verbose_name='Продукт', related_name='recommendations_detail')

    class Meta:
        verbose_name = 'рекомендация'
        verbose_name_plural = 'рекомендации'

    def __str__(self):
        return f'{self.name}'


class NewProduct(models.Model):
    name = models.CharField('Название', max_length=100)
    products = models.OneToOneField(Product, verbose_name='Продукт', related_name='new_product', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Новый продукт'
        verbose_name_plural = 'Новый продукт'

    def __str__(self):
        return f'{self.name}'


class Ordering(models.Model):

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'

    full_name = models.CharField('Фио', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=20)
    region = models.CharField('Область', max_length=100)
    address = models.CharField('Адрес', max_length=100)
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    basket = models.TextField('Корзина')

    def __str__(self):
        return f'{self.full_name}'


class Contact(models.Model):

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    email = models.EmailField('Email', **parametersForNull)
    whatsapp = models.CharField('Whatsapp|Номер телефона', **parametersForNull, max_length=100)
    telegram = models.CharField('Telegram', **parametersForNull, max_length=100)
    instagram = models.URLField('Instagram|URL', **parametersForNull)

    number_main = models.CharField('Главный номер телефона', **parametersForNull, max_length=100)
    number_two = models.CharField('Номер телефона', **parametersForNull, max_length=100)

    def __str__(self):
        return f'{self.email}, {self.whatsapp}, {self.telegram}, {self.instagram}, {self.number_main}, {self.number_two}'

from django.db import models

from .utilities import get_timestamp_path


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL"
    )
    image = models.ImageField(
        upload_to='goods/images/',
        verbose_name='Картинка'
    )
    order = models.SmallIntegerField(
        default=0,
        db_index=True,
        verbose_name='Порядок'
    )
    super_category = models.ForeignKey(
        'SuperCategory',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Категория'
    )


class SuperCategoryManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(super_category__isnull=True)


class SuperCategory(Category):
    objects = SuperCategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('order', 'name')
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

class SubCategoryManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(super_category__isnull=False)


class SubCategory(Category):
    objects = SubCategoryManager()
    
    def __str__(self):
        return f'{self.super_category.name} - {self.name}'


    class Meta:
        proxy = True
        ordering = (
            'super_category__order', 'super_category__name','order', 'name')
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегория'


class Goods(models.Model):
    title = models.CharField(
        max_length=40,
        verbose_name='Товар'
    )
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        verbose_name='Подкатегория'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="Slug"
    )
    price = models.FloatField(
        default=0,
        verbose_name='Цена'
    )
    image = models.ImageField(
        blank=True,
        upload_to=get_timestamp_path,
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

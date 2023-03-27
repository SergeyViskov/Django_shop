from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        unique=True,
        verbose_name='Название'
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


# class Bb(models.Model):
#     rubric = models.ForeignKey(
#         SubCategory,
#         on_delete=models.PROTECT,
#         verbose_name='Рубрика'
#     )
#     title = models.CharField(
#         max_length=40,
#         verbose_name='Товар'
#     )
#     content = models.TextField(
#         verbose_name='Описание'
#     )
#     price = models.FloatField(
#         default=0,
#         verbose_name='Цена'
#     )
#     image = models.ImageField(
#         blank=True,
#         upload_to=get_timestamp_path,
#         verbose_name='Изображение'
#     )
#     author = models.ForeignKey(
#         AdvUser,
#         on_delete=models.CASCADE,
#         verbose_name='Автор объявления'
#     )
#     is_active = models.BooleanField(
#         default=True,
#         db_index=True,
#         verbose_name='Выводить в списке?'
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         db_index=True,
#         verbose_name='Опубликовано'
#     )

#     def delete(self, *args, **kwargs):
#         for ai in self.additionalimage_set.all():
#             ai.delete()
#         super().delete(*args, **kwargs)
    
#     class Meta:
#         verbose_name_plural = 'Объявления'
#         verbose_name = 'Объявление'
#         ordering  =['-created_at']


# class AdditionalImage(models.Model):
#     bb = models.ForeignKey(
#         Bb,
#         on_delete=models.CASCADE,
#         verbose_name='Объявление'
#     )
#     image = models.ImageField(
#         upload_to=get_timestamp_path,
#         verbose_name='Изображение'
#     )

#     class Meta:
#         verbose_name_plural = 'Дополнительные иллюстрации'
#         verbose_name = 'Дополнительная иллюстрация'

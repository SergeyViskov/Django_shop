from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from versatileimagefield.fields import VersatileImageField, PPOIField

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
    image = VersatileImageField(
        'Image',
        upload_to=get_timestamp_path,
        ppoi_field='image_ppoi',
    )
    image_ppoi = PPOIField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username) + ' ' + str(self.total_price)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username) + ' ' + str(self.goods.title)


@receiver(pre_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_goods = Goods.objects.get(id=cart_items.goods.id)
    cart_items.price = int(cart_items.quantity) * float(price_of_goods.price)
    # total_cart_items = CartItems.objects.filter(user=cart_items.user)
    # cart_items.total_items = len(total_cart_items)
    # cart = Cart.objects.get(id=cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()

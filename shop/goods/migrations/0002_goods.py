# Generated by Django 3.2.7 on 2023-03-28 08:40

from django.db import migrations, models
import django.db.models.deletion
import goods.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Товар')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, upload_to=goods.utilities.get_timestamp_path, verbose_name='Изображение')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.subcategory', verbose_name='Подкатегория')),
            ],
        ),
    ]

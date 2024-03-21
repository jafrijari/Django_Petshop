# Generated by Django 5.0.1 on 2024-02-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.CharField(default='Paws', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(default='Product Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='Product Name', max_length=100),
        ),
    ]

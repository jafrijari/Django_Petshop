# Generated by Django 5.0.3 on 2024-03-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_order_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='abc@email.com', max_length=255),
        ),
    ]
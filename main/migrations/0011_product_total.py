# Generated by Django 4.0.4 on 2022-11-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_product_mani_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
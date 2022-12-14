# Generated by Django 4.0.4 on 2022-11-05 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_product_mani_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mani',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='upc',
            field=models.IntegerField(),
        ),
    ]

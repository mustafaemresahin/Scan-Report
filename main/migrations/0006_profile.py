# Generated by Django 4.0.4 on 2022-11-03 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('name', models.TextField()),
                ('last', models.TextField()),
                ('email', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]

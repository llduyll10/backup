# Generated by Django 3.0.7 on 2020-07-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_remove_filmpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmpost',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20200701_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='filmpost',
            name='date_published',
            field=models.DateTimeField(blank=True, verbose_name='date published'),
        ),
    ]

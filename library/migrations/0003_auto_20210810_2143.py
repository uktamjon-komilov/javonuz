# Generated by Django 3.2.6 on 2021-08-10 16:43

from django.db import migrations, models
import library.utils


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20210810_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobook',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=library.utils.get_thumbnail_path),
        ),
        migrations.AddField(
            model_name='paperback',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=library.utils.get_thumbnail_path),
        ),
    ]

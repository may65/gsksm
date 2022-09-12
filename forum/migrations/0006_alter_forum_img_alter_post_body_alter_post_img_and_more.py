# Generated by Django 4.0.6 on 2022-09-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_rename_date_create_forum_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=1024, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d/', verbose_name='фото'),
        ),
    ]
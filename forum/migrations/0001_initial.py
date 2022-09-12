# Generated by Django 4.0.6 on 2022-07-16 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum', models.CharField(max_length=255, verbose_name='Название форума')),
                ('desc', models.CharField(max_length=255, verbose_name='Описание форума')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='изменен')),
            ],
            options={
                'verbose_name': 'Форум',
                'verbose_name_plural': 'Форумы',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255, verbose_name='Тема')),
                ('desc', models.CharField(max_length=255, verbose_name='Описание')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='изменен')),
                ('file', models.FileField(blank=True, null=True, upload_to='file/%Y/%m/%d/', verbose_name='Файл')),
                ('body', models.TextField(max_length=1024)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_topic', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
    ]
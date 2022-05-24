# Generated by Django 3.0 on 2022-05-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('permalink', models.CharField(max_length=12, unique=True, verbose_name='Постоянная ссылка')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='Последняя публикация')),
                ('body_text', models.TextField(blank=True, verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]
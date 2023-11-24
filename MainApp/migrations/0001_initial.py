# Generated by Django 3.2.23 on 2023-11-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('author', models.CharField(max_length=60, verbose_name='Автор')),
                ('year', models.DateField(auto_now_add=True, verbose_name='Дата издания')),
                ('isbn', models.BigIntegerField(default=0, verbose_name='Книжный номер')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]

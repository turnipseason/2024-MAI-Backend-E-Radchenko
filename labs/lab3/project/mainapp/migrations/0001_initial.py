# Generated by Django 5.0.4 on 2024-05-06 10:56

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scientist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ФИО', max_length=200)),
                ('birth_year', models.DateField(default=datetime.date(1990, 1, 1), help_text='Дата рождения')),
                ('country', models.CharField(blank=True, help_text='Страна', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('discovery_year', models.DateField(default=datetime.date(1990, 1, 1), help_text='Год открытия')),
                ('scientist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minerals', to='mainapp.scientist')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название монографии', max_length=60)),
                ('publishing_year', models.DateField(default=datetime.date(1990, 1, 1), help_text='Год выпуска')),
                ('description', models.TextField(default='Описание книги', help_text='Описание')),
                ('authors', models.ManyToManyField(related_name='books', to='mainapp.scientist')),
            ],
        ),
    ]
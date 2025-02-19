# Generated by Django 5.1.2 on 2024-10-18 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('image_url', models.URLField(blank=True, max_length=255, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('fans_count', models.IntegerField(default=0)),
                ('ratings_count', models.IntegerField(default=0)),
                ('average_rating', models.FloatField(default=0.0)),
                ('text_reviews_count', models.IntegerField(default=0)),
                ('works_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(blank=True, max_length=20, null=True)),
                ('isbn13', models.CharField(blank=True, max_length=20, null=True)),
                ('language', models.CharField(blank=True, max_length=10, null=True)),
                ('average_rating', models.FloatField(default=0.0)),
                ('ratings_count', models.IntegerField(default=0)),
                ('text_reviews_count', models.IntegerField(default=0)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('original_publication_date', models.DateField(blank=True, null=True)),
                ('format', models.CharField(blank=True, max_length=50, null=True)),
                ('edition_information', models.CharField(blank=True, max_length=20, null=True)),
                ('image_url', models.URLField(blank=True, max_length=255, null=True)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('num_pages', models.IntegerField(default=0)),
                ('series_position', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('review', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.series'),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_id', models.CharField(max_length=20, unique=True)),
                ('ratings_count', models.IntegerField(default=0)),
                ('average_rating', models.FloatField(default=0.0)),
                ('text_reviews_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.work'),
        ),
        migrations.CreateModel(
            name='BookAuthors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
            options={
                'unique_together': {('book', 'author')},
            },
        ),
        migrations.CreateModel(
            name='BookShelves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.shelf')),
            ],
            options={
                'unique_together': {('book', 'shelf')},
            },
        ),
    ]

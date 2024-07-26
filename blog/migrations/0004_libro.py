# Generated by Django 5.0.7 on 2024-07-25 10:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_excerpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('editorial', models.CharField(max_length=255)),
                ('ano', models.PositiveIntegerField()),
                ('nivel', models.CharField(max_length=50)),
                ('enlace', models.URLField()),
                ('resumen', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='libros/')),
            ],
        ),
    ]

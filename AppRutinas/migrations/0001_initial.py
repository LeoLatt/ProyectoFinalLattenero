# Generated by Django 4.1.3 on 2022-12-18 05:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('cuerpo', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]

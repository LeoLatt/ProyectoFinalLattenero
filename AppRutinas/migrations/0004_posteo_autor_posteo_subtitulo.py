# Generated by Django 4.1.3 on 2022-12-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRutinas', '0003_posteo_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='autor',
            field=models.CharField(default='Leo', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posteo',
            name='subtitulo',
            field=models.CharField(default='subtitulo', max_length=255),
            preserve_default=False,
        ),
    ]

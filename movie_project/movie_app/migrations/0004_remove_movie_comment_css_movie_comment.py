# Generated by Django 4.2.3 on 2023-08-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_movie_viewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comment.css',
        ),
        migrations.AddField(
            model_name='movie',
            name='comment',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
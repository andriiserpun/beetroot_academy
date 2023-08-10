# Generated by Django 4.2.3 on 2023-08-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('reminder', models.DateTimeField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]

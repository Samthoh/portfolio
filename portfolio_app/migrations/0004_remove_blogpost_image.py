# Generated by Django 5.1.6 on 2025-02-12 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_blogpost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='image',
        ),
    ]

# Generated by Django 2.2.12 on 2021-09-03 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippets',
        ),
    ]

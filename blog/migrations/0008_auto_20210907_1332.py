# Generated by Django 2.2.12 on 2021-09-07 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210907_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_category',
            old_name='slug_cat',
            new_name='slug',
        ),
    ]

# Generated by Django 5.0.6 on 2024-08-07 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_rename_create_by_link_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create_by',
            new_name='created_by',
        ),
    ]

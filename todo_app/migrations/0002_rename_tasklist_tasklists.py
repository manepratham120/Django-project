# Generated by Django 4.2.2 on 2023-06-28 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasklist',
            new_name='tasklists',
        ),
    ]

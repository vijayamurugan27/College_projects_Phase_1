# Generated by Django 4.1.4 on 2022-12-18 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_courses'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-16 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_contacts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
    ]

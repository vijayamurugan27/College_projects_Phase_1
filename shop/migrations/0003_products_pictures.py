# Generated by Django 4.1.3 on 2022-12-08 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_person_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]

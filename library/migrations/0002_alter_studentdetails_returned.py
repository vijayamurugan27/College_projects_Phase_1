# Generated by Django 4.1.3 on 2022-12-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]

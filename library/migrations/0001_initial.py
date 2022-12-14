# Generated by Django 4.1.3 on 2022-12-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=1)),
                ('book', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('BookNumber', models.IntegerField()),
                ('Issued_date', models.DateField(auto_now_add=True)),
                ('returned', models.BooleanField()),
                ('returned_date', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]

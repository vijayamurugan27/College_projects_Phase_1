# Generated by Django 4.1.4 on 2022-12-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_remove_blog_message_blog_message1_blog_message10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('expertise', models.CharField(max_length=20)),
                ('experience', models.IntegerField()),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
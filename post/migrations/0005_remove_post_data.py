# Generated by Django 3.2.7 on 2021-09-25 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210925_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='data',
        ),
    ]

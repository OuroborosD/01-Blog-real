# Generated by Django 3.2.7 on 2021-09-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('criacao', models.DateTimeField(auto_now=True)),
                ('autor', models.CharField(max_length=50)),
                ('texto', models.TextField()),
            ],
        ),
    ]
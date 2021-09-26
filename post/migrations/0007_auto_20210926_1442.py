# Generated by Django 3.2.7 on 2021-09-26 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20210926_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comentarios',
        ),
        migrations.AddField(
            model_name='comentario',
            name='post_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]

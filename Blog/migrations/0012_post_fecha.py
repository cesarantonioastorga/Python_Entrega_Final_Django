# Generated by Django 4.0.3 on 2022-04-23 04:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

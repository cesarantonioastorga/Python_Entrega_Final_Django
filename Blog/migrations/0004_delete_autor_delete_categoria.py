# Generated by Django 4.0.3 on 2022-04-21 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
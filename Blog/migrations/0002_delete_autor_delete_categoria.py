# Generated by Django 4.0.3 on 2022-04-21 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
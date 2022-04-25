# Generated by Django 4.0.3 on 2022-04-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Signup', '0002_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=50)),
                ('contraseña1', models.CharField(max_length=20)),
                ('contraseña2', models.CharField(max_length=20)),
            ],
        ),
    ]
# Generated by Django 4.0.1 on 2022-01-23 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppCoder', '0002_delete_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='reseñas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mensaje', models.CharField(max_length=300)),
                ('Email', models.EmailField(max_length=300)),
                ('Fecha', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
    ]

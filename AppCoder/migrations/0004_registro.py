# Generated by Django 4.0.1 on 2022-01-24 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('fechaDeNacimiento', models.DateField()),
            ],
        ),
    ]

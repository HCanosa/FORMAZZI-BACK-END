# Generated by Django 3.2.25 on 2024-11-03 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('empresa_pertencente', models.CharField(max_length=255)),
                ('id_empresa_pertencente', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
    ]
# Generated by Django 4.2.6 on 2024-05-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('preco', models.FloatField(default=0.0)),
                ('descricao', models.CharField(max_length=256)),
                ('categoria', models.CharField(choices=[('Bebidas', 'Bebidas'), ('Hambúrgueres', 'Hambúrgueres'), ('Pizzas', 'Pizzas')], default='Bebidas', max_length=30)),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2025-01-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comida', '0010_alter_platillo_precio_alter_platillo_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platillo',
            name='fecha_disponible',
            field=models.DateField(),
        ),
    ]

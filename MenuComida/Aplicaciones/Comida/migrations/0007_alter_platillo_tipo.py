# Generated by Django 4.0.6 on 2024-12-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comida', '0006_platillo_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platillo',
            name='tipo',
            field=models.CharField(choices=[('Sopa', 'Sopa'), ('Segundo', 'Segundo'), ('Jugo', 'Jugo'), ('Postre', 'Postre'), ('Otro', 'Otro')], default='otro', max_length=20),
        ),
    ]

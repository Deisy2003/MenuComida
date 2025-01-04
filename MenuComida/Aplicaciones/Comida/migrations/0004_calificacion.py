# Generated by Django 4.0.6 on 2024-12-23 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Comida', '0003_delete_calificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('calificacion', models.IntegerField(choices=[(1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comida.platillo')),
            ],
        ),
    ]

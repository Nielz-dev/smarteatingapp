# Generated by Django 3.2 on 2023-06-02 14:23

from django.db import migrations, models
import smartEatingApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('smartEatingApp', '0002_plato_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='foto_perfil',
            field=models.URLField(default=smartEatingApp.models.generate_random_foto_perfil, max_length=350),
        ),
    ]

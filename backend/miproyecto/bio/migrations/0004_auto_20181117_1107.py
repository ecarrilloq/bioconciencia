# Generated by Django 2.1 on 2018-11-17 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0003_denuncia_georeferencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='IdDireccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='IdPerfil',
        ),
    ]

# Generated by Django 2.1 on 2018-11-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_auto_20181115_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='Georeferencia',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

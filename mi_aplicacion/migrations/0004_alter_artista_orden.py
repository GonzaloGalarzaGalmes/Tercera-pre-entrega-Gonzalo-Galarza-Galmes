# Generated by Django 4.2 on 2024-08-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0003_artista_orden_alter_album_table_alter_artista_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='orden',
            field=models.IntegerField(default=1),
        ),
    ]

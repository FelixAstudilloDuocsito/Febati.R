# Generated by Django 5.0.6 on 2024-07-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Febati_APP_85', '0003_comentar_rename_correo_usuario_correo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

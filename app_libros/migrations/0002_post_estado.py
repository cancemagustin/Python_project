# Generated by Django 5.1.4 on 2024-12-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='estado',
            field=models.CharField(choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='borrador', max_length=50),
        ),
    ]

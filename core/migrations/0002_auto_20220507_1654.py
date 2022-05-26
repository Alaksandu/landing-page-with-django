# Generated by Django 3.2.13 on 2022-05-07 19:54

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='twiiter',
            new_name='twitter',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-05 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0002_auto_20210201_2339'),
        ('submissoes', '0003_submissao_pergunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='pergunta',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='perguntas.pergunta'),
        ),
    ]

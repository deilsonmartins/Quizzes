# Generated by Django 3.1.6 on 2021-02-05 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0002_auto_20210201_2339'),
        ('respostas', '0002_resposta_pergunta'),
        ('submissoes', '0005_auto_20210205_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissao',
            name='questionario',
        ),
        migrations.RemoveField(
            model_name='submissao',
            name='score',
        ),
        migrations.AddField(
            model_name='submissao',
            name='acertou',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissao',
            name='resposta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='respostas.resposta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submissao',
            name='pergunta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='perguntas.pergunta'),
            preserve_default=False,
        ),
    ]

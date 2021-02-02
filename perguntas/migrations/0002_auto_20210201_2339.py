# Generated by Django 3.1.6 on 2021-02-01 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0002_remove_questionario_perguntas'),
        ('perguntas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='respostas',
        ),
        migrations.AddField(
            model_name='pergunta',
            name='questionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questionarios.questionario'),
            preserve_default=False,
        ),
    ]

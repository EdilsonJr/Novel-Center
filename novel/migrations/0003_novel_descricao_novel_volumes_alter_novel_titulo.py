# Generated by Django 4.0.4 on 2022-05-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0002_novel_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='descricao',
            field=models.TextField(default='aaaa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='novel',
            name='volumes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='novel',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='Título'),
        ),
    ]

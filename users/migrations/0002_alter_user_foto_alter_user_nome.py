# Generated by Django 4.0.4 on 2022-06-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(default='s', upload_to='user_foto/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]

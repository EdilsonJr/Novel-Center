# Generated by Django 4.0.4 on 2022-06-15 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0003_alter_novel_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
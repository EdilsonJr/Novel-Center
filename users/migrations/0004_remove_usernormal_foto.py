# Generated by Django 4.0.4 on 2022-06-09 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_user_usernormal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usernormal',
            name='foto',
        ),
    ]
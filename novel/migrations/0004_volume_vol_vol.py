# Generated by Django 4.0.4 on 2022-06-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0003_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='volume',
            name='vol_vol',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
    ]
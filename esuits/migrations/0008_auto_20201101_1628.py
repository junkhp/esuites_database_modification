# Generated by Django 3.0.8 on 2020-11-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esuits', '0007_auto_20201101_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='char_num',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

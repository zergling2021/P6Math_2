# Generated by Django 3.1.7 on 2021-08-09 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0025_auto_20210809_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='sciencequestion',
            name='image2_name',
            field=models.CharField(default='000_02.png', max_length=200),
        ),
    ]

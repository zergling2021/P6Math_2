# Generated by Django 3.1.7 on 2021-06-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0007_auto_20210623_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sciencequestion',
            name='image_name',
            field=models.CharField(default='000_01.png', max_length=200),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='question_model',
            field=models.CharField(default='NA', max_length=2000),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='question_model_index',
            field=models.CharField(default='0000', max_length=200),
        ),
    ]

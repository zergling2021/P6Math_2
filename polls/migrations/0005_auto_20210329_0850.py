# Generated by Django 3.1.7 on 2021-03-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210328_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='attempted_answer',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210323_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='attempted_answer',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(default='', max_length=20),
        ),
    ]
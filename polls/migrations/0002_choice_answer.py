# Generated by Django 3.1.7 on 2021-03-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='answer',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
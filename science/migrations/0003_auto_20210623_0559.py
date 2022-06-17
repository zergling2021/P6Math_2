# Generated by Django 3.1.7 on 2021-06-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0002_auto_20210622_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='sciencequestion',
            name='number_of_attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sciencequestion',
            name='number_of_successful_attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sciencequestion',
            name='subtopic_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='sciencequestion',
            name='topic_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]

# Generated by Django 3.1.7 on 2021-06-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0010_sciencequestion_lv3_topic_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='sciencequestion',
            name='success_on_first_attempt',
            field=models.CharField(default='No', max_length=10),
        ),
    ]

# Generated by Django 3.1.7 on 2021-06-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0016_auto_20210628_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sciencequestion',
            name='lv3_topic_number',
            field=models.CharField(default='0', max_length=50),
        ),
    ]

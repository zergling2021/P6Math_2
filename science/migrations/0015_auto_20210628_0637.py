# Generated by Django 3.1.7 on 2021-06-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0014_auto_20210627_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_index', models.CharField(default='0', max_length=10)),
                ('topic_name', models.CharField(default='0', max_length=500)),
                ('number_of_questions', models.IntegerField(default=0)),
                ('number_of_success_first_attempt', models.IntegerField(default=0)),
                ('number_of_latest_success_attempt', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='sciencequestion',
            name='last_attempt_success',
            field=models.CharField(default='No', max_length=50),
        ),
    ]

# Generated by Django 3.1.7 on 2021-08-08 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0020_sciencequestion_answer_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sciencequestion',
            name='question_subject',
            field=models.CharField(default='Science', max_length=200),
        ),
        migrations.AddField(
            model_name='sciencequestion',
            name='question_type',
            field=models.CharField(default='MCQ', max_length=200),
        ),
    ]

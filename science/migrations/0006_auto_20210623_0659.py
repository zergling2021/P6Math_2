# Generated by Django 3.1.7 on 2021-06-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0005_auto_20210623_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sciencequestion',
            name='question_additional_text_line_1',
            field=models.CharField(default='*', max_length=500),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='question_additional_text_line_2',
            field=models.CharField(default='*', max_length=500),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='question_additional_text_line_3',
            field=models.CharField(default='*', max_length=500),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='question_additional_text_line_4',
            field=models.CharField(default='*', max_length=500),
        ),
    ]
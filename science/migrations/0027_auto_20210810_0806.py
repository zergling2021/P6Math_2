# Generated by Django 3.1.7 on 2021-08-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0026_sciencequestion_image2_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sciencequestion',
            name='attempted_answer_d',
            field=models.CharField(default='0', max_length=500),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='attempted_answer_a',
            field=models.CharField(default='0', max_length=500),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='attempted_answer_b',
            field=models.CharField(default='0', max_length=500),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='attempted_answer_c',
            field=models.CharField(default='0', max_length=500),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='correct_answer_b',
            field=models.CharField(default='0', max_length=500),
        ),
        migrations.AlterField(
            model_name='sciencequestion',
            name='correct_answer_c',
            field=models.CharField(default='0', max_length=500),
        ),
    ]

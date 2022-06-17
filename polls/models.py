from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_model_index = models.CharField(max_length=200, default='')
    question_model = models.CharField(max_length=2000, default='')
    question_text = models.CharField(max_length=2000, default='')
    pub_date = models.DateTimeField('date published')
    correct_answer_a = models.CharField(max_length=20, default='0')
    attempted_answer_a = models.CharField(max_length=20, default='0')
    correct_answer_b = models.CharField(max_length=20, default='0')
    attempted_answer_b = models.CharField(max_length=20, default='0')
    correct_answer_c = models.CharField(max_length=20, default='0')
    attempted_answer_c = models.CharField(max_length=20, default='0')
    result_text = models.CharField(max_length=2000, default='')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    answer = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
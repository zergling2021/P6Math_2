import datetime

from django.db import models
from django.db.models import Model
from django.utils import timezone


class ScienceQuestion(models.Model):
    question_model_index = models.CharField(max_length=200, default='000')
    question_model = models.CharField(max_length=2000, default='NA')
    question_text = models.CharField(max_length=2000, default='*')
    pub_date = models.DateTimeField('date published')
    correct_answer_a = models.CharField(max_length=20, default='0')
    attempted_answer_a = models.CharField(max_length=500, default='0')
    correct_answer_b = models.CharField(max_length=500, default='0')
    attempted_answer_b = models.CharField(max_length=500, default='0')
    correct_answer_c = models.CharField(max_length=500, default='0')
    attempted_answer_c = models.CharField(max_length=500, default='0')
    attempted_answer_d = models.CharField(max_length=500, default='0')
    result_text = models.CharField(max_length=2000, default='')
    topic_number = models.CharField(max_length=20, default='1')
    subtopic_number = models.CharField(max_length=50, default='1')
    lv3_topic_number = models.CharField(max_length=50, default='0')
    number_of_attempts = models.IntegerField(default=0)
    number_of_successful_attempts = models.IntegerField(default=0)
    image_name = models.CharField(max_length=200, default='000_01.png')
    image2_name = models.CharField(max_length=200, default='000_02.png')
    question_additional_text_line_1 = models.CharField(max_length=500, default='*')
    question_additional_text_line_2 = models.CharField(max_length=500, default='*')
    question_additional_text_line_3 = models.CharField(max_length=500, default='*')
    question_additional_text_line_4 = models.CharField(max_length=500, default='*')
    question_source = models.CharField(max_length=100, default='')
    success_on_first_attempt = models.CharField(max_length=10, default='No')
    last_attempt_date = models.CharField(max_length=50, default='0')
    last_attempt_success = models.CharField(max_length=50, default='No')
    first_self_rated_score = models.IntegerField(default=-1)
    latest_self_rated_score = models.IntegerField(default=-1)
    answer_image_name = models.CharField(max_length=200, default='default_pic.png')
    question_type = models.CharField(max_length=200, default='MCQ')
    question_subject = models.CharField(max_length=200, default='Science')

    #pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class ScienceChoice(models.Model):
    question = models.ForeignKey(ScienceQuestion, on_delete=models.CASCADE)
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

class ScienceTopic(models.Model):
    topic_index = models.CharField(max_length=10, default='0')
    topic_name = models.CharField(max_length=500, default='0')
    number_of_questions = models.IntegerField(default=0)
    number_of_attempted_questions = models.IntegerField(default=0)
    number_of_success_first_attempt = models.IntegerField(default=0)
    number_of_latest_success_attempt = models.IntegerField(default=0)
    number_of_attempted_open_questions = models.IntegerField(default=0)
    avg_first_self_rated_score = models.FloatField(default=0.0)
    avg_latest_self_rated_score = models.FloatField(default=0.0)


class ScienceSubTopic(models.Model):
    topic_index = models.CharField(max_length=10, default='0')
    topic_name = models.CharField(max_length=500, default='0')
    number_of_questions = models.IntegerField(default=0)
    number_of_attempted_questions = models.IntegerField(default=0)
    number_of_success_first_attempt = models.IntegerField(default=0)
    number_of_latest_success_attempt = models.IntegerField(default=0)
    number_of_attempted_open_questions = models.IntegerField(default=0)
    avg_first_self_rated_score = models.FloatField(default=0.0)
    avg_latest_self_rated_score = models.FloatField(default=0.0)

class ScienceLevel3Topic(models.Model):
    topic_index = models.CharField(max_length=10, default='0')
    topic_name = models.CharField(max_length=500, default='0')
    number_of_questions = models.IntegerField(default=0)
    number_of_attempted_questions = models.IntegerField(default=0)
    number_of_success_first_attempt = models.IntegerField(default=0)
    number_of_latest_success_attempt = models.IntegerField(default=0)
    number_of_attempted_open_questions = models.IntegerField(default=0)
    avg_first_self_rated_score = models.FloatField(default=0.0)
    avg_latest_self_rated_score = models.FloatField(default=0.0)


#English

class EnglishQuestion(models.Model):
    question_model_index = models.CharField(max_length=200, default='000')
    question_model = models.CharField(max_length=2000, default='NA')
    question_text = models.CharField(max_length=2000, default='*')
    pub_date = models.DateTimeField('date published')
    correct_answer_a = models.CharField(max_length=20, default='0')
    attempted_answer_a = models.CharField(max_length=500, default='0')
    correct_answer_b = models.CharField(max_length=500, default='0')
    attempted_answer_b = models.CharField(max_length=500, default='0')
    correct_answer_c = models.CharField(max_length=500, default='0')
    attempted_answer_c = models.CharField(max_length=500, default='0')
    attempted_answer_d = models.CharField(max_length=500, default='0')
    result_text = models.CharField(max_length=2000, default='')
    topic_number = models.CharField(max_length=20, default='1')
    subtopic_number = models.CharField(max_length=50, default='1')
    lv3_topic_number = models.CharField(max_length=50, default='0')
    number_of_attempts = models.IntegerField(default=0)
    number_of_successful_attempts = models.IntegerField(default=0)
    image_name = models.CharField(max_length=200, default='000_01.png')
    image2_name = models.CharField(max_length=200, default='000_02.png')
    question_additional_text_line_1 = models.CharField(max_length=500, default='*')
    question_additional_text_line_2 = models.CharField(max_length=500, default='*')
    question_additional_text_line_3 = models.CharField(max_length=500, default='*')
    question_additional_text_line_4 = models.CharField(max_length=500, default='*')
    question_source = models.CharField(max_length=100, default='')
    success_on_first_attempt = models.CharField(max_length=10, default='No')
    last_attempt_date = models.CharField(max_length=50, default='0')
    last_attempt_success = models.CharField(max_length=50, default='No')
    first_self_rated_score = models.IntegerField(default=-1)
    latest_self_rated_score = models.IntegerField(default=-1)
    answer_image_name = models.CharField(max_length=200, default='default_pic.png')
    question_type = models.CharField(max_length=200, default='MCQ')
    question_subject = models.CharField(max_length=200, default='Science')



    #pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class EnglishChoice(models.Model):
    question = models.ForeignKey(ScienceQuestion, on_delete=models.CASCADE)
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

class EnglishTopic(models.Model):
    topic_index = models.CharField(max_length=10, default='0')
    topic_name = models.CharField(max_length=500, default='0')
    number_of_questions = models.IntegerField(default=0)
    number_of_attempted_questions = models.IntegerField(default=0)
    number_of_success_first_attempt = models.IntegerField(default=0)
    number_of_latest_success_attempt = models.IntegerField(default=0)
    number_of_attempted_open_questions = models.IntegerField(default=0)
    avg_first_self_rated_score = models.FloatField(default=0.0)
    avg_latest_self_rated_score = models.FloatField(default=0.0)


class EnglishSubTopic(models.Model):
    topic_index = models.CharField(max_length=10, default='0')
    topic_name = models.CharField(max_length=500, default='0')
    number_of_questions = models.IntegerField(default=0)
    number_of_attempted_questions = models.IntegerField(default=0)
    number_of_success_first_attempt = models.IntegerField(default=0)
    number_of_latest_success_attempt = models.IntegerField(default=0)
    number_of_attempted_open_questions = models.IntegerField(default=0)
    avg_first_self_rated_score = models.FloatField(default=0.0)
    avg_latest_self_rated_score = models.FloatField(default=0.0)

class EnglishLevel3Topic(models.Model):
    topic_index = models.CharField(max_length=10, default='0')
    topic_name = models.CharField(max_length=500, default='0')
    number_of_questions = models.IntegerField(default=0)
    number_of_attempted_questions = models.IntegerField(default=0)
    number_of_success_first_attempt = models.IntegerField(default=0)
    number_of_latest_success_attempt = models.IntegerField(default=0)
    number_of_attempted_open_questions = models.IntegerField(default=0)
    avg_first_self_rated_score = models.FloatField(default=0.0)
    avg_latest_self_rated_score = models.FloatField(default=0.0)


class UserProfile(models.Model):
    user_id = models.CharField(max_length=50, default='0')
    user_name = models.CharField(max_length=200, default='0')
    user_school = models.CharField(max_length=200, default='0')
    user_grade = models.CharField(max_length=200, default='0')
    user_mailing_address = models.CharField(max_length=200, default='0')
    user_contact_no = models.CharField(max_length=30, default='0')
    user_email_address = models.CharField(max_length=200, default='0')

class AnswerRecords(models.Model):
    user_id = models.CharField(max_length=50, default='0')
    question_model_index = models.CharField(max_length=200, default='000')
    question_model = models.CharField(max_length=2000, default='NA')
    question_text = models.CharField(max_length=2000, default='*')
    record_date = models.DateTimeField('date recorded')
    correct_answer_a = models.CharField(max_length=20, default='0')
    attempted_answer_a = models.CharField(max_length=500, default='0')
    correct_answer_b = models.CharField(max_length=500, default='0')
    attempted_answer_b = models.CharField(max_length=500, default='0')
    correct_answer_c = models.CharField(max_length=500, default='0')
    attempted_answer_c = models.CharField(max_length=500, default='0')
    mcq_answer_successful = models.CharField(max_length=10, default='0')
    result_text = models.CharField(max_length=2000, default='')
    topic_number = models.CharField(max_length=20, default='1')
    subtopic_number = models.CharField(max_length=50, default='1')
    lv3_topic_number = models.CharField(max_length=50, default='0')
    self_rated_score = models.IntegerField(default=-1)
    question_type = models.CharField(max_length=200, default='MCQ')
    question_subject = models.CharField(max_length=200, default='Science')



from django.contrib import admin

# Register your models here.
from .models import ScienceQuestion, ScienceChoice, ScienceTopic, ScienceSubTopic, ScienceLevel3Topic
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = ScienceChoice
    extra = 10


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Model Index', {'fields': ['question_model_index']}),
        ('Question Subject', {'fields': ['question_subject']}),
        ('Question Type', {'fields': ['question_type']}),
        ('Question Model', {'fields': ['question_model']}),
        (None,              {'fields': ['question_text']}),
        ('Question Text Additional Line 1', {'fields': ['question_additional_text_line_1']}),
        ('Question Text Additional Line 2', {'fields': ['question_additional_text_line_2']}),
        ('Question Text Additional Line 3', {'fields': ['question_additional_text_line_3']}),
        ('Question Text Additional Line 4', {'fields': ['question_additional_text_line_4']}),
        ('Question Source', {'fields': ['question_source']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Correct Answer a', {'fields': ['correct_answer_a']}),
        ('Correct Answer b', {'fields': ['correct_answer_b']}),
        ('Correct Answer c', {'fields': ['correct_answer_c']}),
        ('Answer Image Name', {'fields': ['answer_image_name']}),
        ('Topic Number', {'fields': ['topic_number']}),
        ('Subtopic Number', {'fields': ['subtopic_number']}),
        ('Level 3 Topic Number', {'fields': ['lv3_topic_number']}),
        ('Total Attempts', {'fields': ['number_of_attempts']}),
        ('Total Successful Attempts', {'fields': ['number_of_successful_attempts']}),
        ('Success on First Attempt?', {'fields': ['success_on_first_attempt']}),
        ('Question Image Name', {'fields': ['image_name']}),
        ('Question Image2 Name', {'fields': ['image2_name']}),
        ('Last Attempt Date', {'fields': ['last_attempt_date']}),
        ('Attempted Answer a', {'fields': ['attempted_answer_a']}),
        ('Attempted Answer b', {'fields': ['attempted_answer_b']}),
        ('Attempted Answer c', {'fields': ['attempted_answer_c']}),
        ('Attempted Answer d', {'fields': ['attempted_answer_d']}),
        ('First Self-Rated Score', {'fields': ['first_self_rated_score']}),
        ('Latest Self-Rated Score', {'fields': ['latest_self_rated_score']}),

    ]
    inlines = [ChoiceInline]
    list_display = ('question_model_index', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Topic Index', {'fields': ['topic_index']}),
        ('Topic Name', {'fields': ['topic_name']}),
        ('Number of Questions', {'fields': ['number_of_questions']}),
        ('Number of Success First Attempt', {'fields': ['number_of_success_first_attempt']}),
        ('Number of Latest Success Attempt', {'fields': ['number_of_latest_success_attempt']}),
    ]
    list_display = ('topic_index', 'topic_name',)


class SubTopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Topic Index', {'fields': ['topic_index']}),
        ('Topic Name', {'fields': ['topic_name']}),
        ('Number of Questions', {'fields': ['number_of_questions']}),
        ('Number of Success First Attempt', {'fields': ['number_of_success_first_attempt']}),
        ('Number of Latest Success Attempt', {'fields': ['number_of_latest_success_attempt']}),
    ]
    list_display = ('topic_index', 'topic_name',)


class Level3TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Topic Index', {'fields': ['topic_index']}),
        ('Topic Name', {'fields': ['topic_name']}),
        ('Number of Questions', {'fields': ['number_of_questions']}),
        ('Number of Success First Attempt', {'fields': ['number_of_success_first_attempt']}),
        ('Number of Latest Success Attempt', {'fields': ['number_of_latest_success_attempt']}),
    ]
    list_display = ('topic_index', 'topic_name',)


admin.site.register(ScienceQuestion, QuestionAdmin)
admin.site.register(ScienceTopic, TopicAdmin)
admin.site.register(ScienceSubTopic, SubTopicAdmin)
admin.site.register(ScienceLevel3Topic, Level3TopicAdmin)


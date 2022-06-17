from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 10


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Model Index', {'fields': ['question_model_index']}),
        ('Question Model', {'fields': ['question_model']}),
        (None,              {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Correct Answer a)', {'fields': ['correct_answer_a']}),
        ('Correct Answer b)', {'fields': ['correct_answer_b']}),
        ('Correct Answer c)', {'fields': ['correct_answer_c']}),

    ]
    inlines = [ChoiceInline]
    list_display = ('question_model_index', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
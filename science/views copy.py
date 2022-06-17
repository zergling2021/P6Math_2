from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
#from .models import Question
from django.urls import reverse
from django.views import generic
from .models import ScienceChoice, ScienceQuestion, ScienceTopic, ScienceSubTopic, ScienceLevel3Topic
from .forms import ReceiveAnswer
from fractions import Fraction
import datetime
import random
import gtts
from playsound import playsound

#def index(request):
#    return HttpResponse("Hello, world. You're at the science index.")


from django.shortcuts import render

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'science/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ScienceQuestion.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5000]


class DetailView(generic.DetailView):
    model = ScienceQuestion
    template_name = 'science/detail.html'



    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError("Generic detail view %s must be called with "
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        #Generate actual question text from question_model, and save it to question_text.

        return obj

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """

        return ScienceQuestion.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = ScienceQuestion
    template_name = 'science/results.html'

class ScienceReportView(generic.ListView):
    template_name = 'science/science_report.html'
    context_object_name = 'failed_question_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ScienceQuestion.objects.filter(question_subject="Science").filter(number_of_attempts__gte=1).filter(success_on_first_attempt="No").order_by('-pub_date')[:5000]

class ScienceMCQView(generic.ListView):
    template_name = 'science/science_mcq.html'
    context_object_name = 'science_mcq_question_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ScienceQuestion.objects.filter(question_subject="Science").filter(question_type="MCQ").order_by('-pub_date')[:5000]

class ScienceOpenView(generic.ListView):
    template_name = 'science/science_open.html'
    context_object_name = 'science_open_question_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ScienceQuestion.objects.filter(question_subject="Science").filter(question_type="Open").order_by('-pub_date')[:5000]

class ScienceReportresultView(generic.ListView):
    template_name = 'science/science_reportresult.html'
    context_object_name = 'level1_topic_list'

    print (datetime.datetime.now())

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ScienceTopic.objects.all()
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['level2_topic_list'] = ScienceSubTopic.objects.all()
        context_data['level3_topic_list'] = ScienceLevel3Topic.objects.all()
        return context_data


def vote(request, question_id):
    question = get_object_or_404(ScienceQuestion, pk=question_id)

    #try:
   #     selected_choice = question.sciencechoice_set.get(pk=request.POST['sciencechoice'])
  #  except (KeyError, ScienceChoice.DoesNotExist):
        # Redisplay the question voting form.
   #     return render(request, 'science/detail.html', {
    #        'sciencequestion': question,
    #        'error_message': "You didn't select a choice.",
    #    })
    #else:
        #selected_choice.votes += 1
        #selected_choice.answer = request.POST.get('answer', 'FFF')
        #selected_choice.answer = request.POST['answer']
    if 1:
        attempted_answer_a = request.POST['attempted_answer_a']
        if attempted_answer_a == '':
            attempted_answer_a = '0'
        attempted_answer_b = request.POST['attempted_answer_b']
        if attempted_answer_b == '':
            attempted_answer_b = '0'
        attempted_answer_c = request.POST['attempted_answer_c']
        if attempted_answer_c == '':
            attempted_answer_c = '0'
        attempted_answer_d = request.POST['attempted_answer_d']
        if attempted_answer_d == '':
            attempted_answer_d = '0'
        self_rated_score = request.POST['self_rated_score']
        if self_rated_score == '':
            self_rated_score = '0'

        question.attempted_answer_a = attempted_answer_a
        question.attempted_answer_b = attempted_answer_b
        question.attempted_answer_c = attempted_answer_c

        #print("Self Rated Score is ", question.self_rated_score)

        #if (float(question.correct_answer_a) == float(attempted_answer_a) and float(question.correct_answer_b) == float(attempted_answer_b) and float(question.correct_answer_c) == float(attempted_answer_c)):
        if(question.question_type == "MCQ"):
            if question.correct_answer_a == attempted_answer_a and question.correct_answer_b == attempted_answer_b and question.correct_answer_c == attempted_answer_c:
                question.result_text = "Your answer is correct!"
                #tts = gtts.gTTS("Congratulations! Your answer is correct!")

                question.last_attempt_success = "Yes"
                question.number_of_attempts = question.number_of_attempts + 1
                question.number_of_successful_attempts = question.number_of_successful_attempts + 1
                if question.number_of_attempts == 1:
                    question.success_on_first_attempt = "Yes"
            else:
                question.result_text = "Your answer is wrong. Correct answer is " + "a) = " + question.correct_answer_a + " b) = " + question.correct_answer_b + " c) = " + question.correct_answer_c + "."
                question.number_of_attempts = question.number_of_attempts + 1
        else:
            question.result_text = "Thank you for submitting answer. Your self-rated score is " + self_rated_score
            question.number_of_attempts = question.number_of_attempts + 1
            if question.number_of_attempts == 1:
                question.first_self_rated_score = self_rated_score
                if(int(self_rated_score) > 7):
                    question.success_on_first_attempt = "Yes"
            question.latest_self_rated_score = self_rated_score

        #tts = gtts.gTTS("Please try again!")
        #tts.save("result.mp3")
        #playsound("result.mp3")
        question.last_attempt_date = datetime.datetime.now()
        question.save()

       # selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('science:results', args=(question.id,)))


def generate_science_report(request):
    #fill in the report content here and show in reportresult.html

    #Clear report statistics
    for topic in ScienceTopic.objects.all():
        topic.number_of_questions = 0
        topic.number_of_attempted_questions = 0
        topic.number_of_success_first_attempt = 0
        topic.number_of_latest_success_attempt = 0
        topic.number_of_attempted_open_questions = 0
        topic.avg_first_self_rated_score = 0.0
        topic.avg_latest_self_rated_score = 0.0
        topic.save()
    for topic in ScienceSubTopic.objects.all():
        topic.number_of_questions = 0
        topic.number_of_attempted_questions = 0
        topic.number_of_success_first_attempt = 0
        topic.number_of_latest_success_attempt = 0
        topic.number_of_attempted_open_questions = 0
        topic.avg_first_self_rated_score = 0.0
        topic.avg_latest_self_rated_score = 0.0
        topic.save()
    for topic in ScienceLevel3Topic.objects.all():
        topic.number_of_questions = 0
        topic.number_of_attempted_questions = 0
        topic.number_of_success_first_attempt = 0
        topic.number_of_latest_success_attempt = 0
        topic.number_of_attempted_open_questions = 0
        topic.avg_first_self_rated_score = 0.0
        topic.avg_latest_self_rated_score = 0.0
        topic.save()
    #clean up question records, turn this on only to clean records
    #for q in ScienceQuestion.objects.all():
    #    print("cleaning up records")
    #    q.number_of_attempts = 0
    #    q.number_of_successful_attempts = 0
    #    q.success_on_first_attempt = "No"
    #    q.first_self_rated_score = -1
    #    q.latest_self_rated_score = -1
    #    q.attempted_answer_a = 0
    #    q.save()
    #end of clean up

    for q in ScienceQuestion.objects.all():
        topiclist = q.topic_number.split(";")
        subtopiclist = q.subtopic_number.split(";")
        level3topiclist = q.lv3_topic_number.split(";")
        if(q.question_subject == "Science" and q.question_type == "MCQ"):
            for topic in ScienceTopic.objects.all():
                #print("Topic level 1: ", topic.topic_index)
                for t in topiclist:
                    #print ("t = ", t)
                    if t == topic.topic_index:
                        #print("Match!")
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                        if q.success_on_first_attempt == "Yes":
                            topic.number_of_success_first_attempt = topic.number_of_success_first_attempt + 1
                            if q.number_of_attempts == 1 and q.last_attempt_success == "No":
                                q.last_attempt_success = "Yes"
                                q.save()
                        if q.last_attempt_success == "Yes":
                            topic.number_of_latest_success_attempt = topic.number_of_latest_success_attempt + 1

                        topic.save()
            for topic in ScienceSubTopic.objects.all():
                #print("Topic level 2: ", topic.topic_index)
                for t in subtopiclist:
                    #print("level 2 t = ", t)
                    if t == topic.topic_index:
                        #print("Match!")
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                        if q.success_on_first_attempt == "Yes":
                            topic.number_of_success_first_attempt = topic.number_of_success_first_attempt + 1
                            if q.number_of_attempts == 1 and q.last_attempt_success == "No":
                                q.last_attempt_success = "Yes"
                                q.save()
                        if q.last_attempt_success == "Yes":
                            topic.number_of_latest_success_attempt = topic.number_of_latest_success_attempt + 1
                        topic.save()
            for topic in ScienceLevel3Topic.objects.all():
                for t in level3topiclist:
                    #print("level 3 t = ", t)
                    if t == topic.topic_index:
                        #print ("Match! ", t)
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                        if q.success_on_first_attempt == "Yes":
                            topic.number_of_success_first_attempt = topic.number_of_success_first_attempt + 1
                            if q.number_of_attempts == 1 and q.last_attempt_success == "No":
                                q.last_attempt_success = "Yes"
                                q.save()
                        if q.last_attempt_success == "Yes":
                            topic.number_of_latest_success_attempt = topic.number_of_latest_success_attempt + 1
                        topic.save()
        #print("before search for open")
        if (q.question_subject == "Science" and q.question_type == "Open"):
           # print("search for Open questions")
            for topic in ScienceTopic.objects.all():
                # print("Topic level 1: ", topic.topic_index)
                for t in topiclist:
                    #print ("t = ", t)
                    if t == topic.topic_index:
                        #print("Match!")
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                            if(q.number_of_attempts == 1):
                                topic.avg_first_self_rated_score = (topic.avg_first_self_rated_score * topic.number_of_attempted_open_questions + q.first_self_rated_score)/(topic.number_of_attempted_open_questions + 1)
                            topic.avg_latest_self_rated_score = (topic.avg_latest_self_rated_score * topic.number_of_attempted_open_questions + q.latest_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.number_of_attempted_open_questions = topic.number_of_attempted_open_questions + 1
                        topic.save()
            for topic in ScienceSubTopic.objects.all():
                # print("Topic level 2: ", topic.topic_index)
                for t in subtopiclist:
                    # print("level 2 t = ", t)
                    if t == topic.topic_index:
                        # print("Match!")
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                            if (q.number_of_attempts == 1):
                                topic.avg_first_self_rated_score = (topic.avg_first_self_rated_score * topic.number_of_attempted_open_questions + q.first_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.avg_latest_self_rated_score = (topic.avg_latest_self_rated_score * topic.number_of_attempted_open_questions + q.latest_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.number_of_attempted_open_questions = topic.number_of_attempted_open_questions + 1
                        topic.save()
            for topic in ScienceLevel3Topic.objects.all():
                for t in level3topiclist:
                    # print("level 3 t = ", t)
                    if t == topic.topic_index:
                        # print ("Match! ", t)
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                            if (q.number_of_attempts == 1):
                                topic.avg_first_self_rated_score = (topic.avg_first_self_rated_score * topic.number_of_attempted_open_questions + q.first_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.avg_latest_self_rated_score = (topic.avg_latest_self_rated_score * topic.number_of_attempted_open_questions + q.latest_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.number_of_attempted_open_questions = topic.number_of_attempted_open_questions + 1
                        topic.save()

    #delete all existing report instances first


    return HttpResponseRedirect(reverse('science:science_reportresult', args=()))

def results(request, question_id):
    question = get_object_or_404(ScienceQuestion, pk=question_id)
    return render(request, 'science/results.html', {'question': question})

def reportresult(request):
    return render(request, 'science/science_reportresult.html')

class EnglishMCQView(generic.ListView):
    template_name = 'science/english_mcq.html'
    context_object_name = 'english_mcq_question_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ScienceQuestion.objects.filter(question_subject="English").filter(question_type="MCQ").order_by('-pub_date')[:5000]
class EnglishOpenView(generic.ListView):
    template_name = 'science/english_open.html'
    context_object_name = 'english_open_question_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ScienceQuestion.objects.filter(question_subject="English").filter(question_type="Open").order_by('-pub_date')[:5000]
class EnglishReportView(generic.ListView):
    template_name = 'science/english_report.html'
    context_object_name = 'failed_question_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ScienceQuestion.objects.filter(question_subject="English").filter(number_of_attempts__gte=1).filter(success_on_first_attempt="No").order_by('-pub_date')[:5000]

def generate_english_report(request):
    #fill in the report content here and show in reportresult.html

    #Clear report statistics
    for topic in ScienceTopic.objects.all():
        topic.number_of_questions = 0
        topic.number_of_attempted_questions = 0
        topic.number_of_success_first_attempt = 0
        topic.number_of_latest_success_attempt = 0
        topic.number_of_attempted_open_questions = 0
        topic.avg_first_self_rated_score = 0.0
        topic.avg_latest_self_rated_score = 0.0
        topic.save()
    for topic in ScienceSubTopic.objects.all():
        topic.number_of_questions = 0
        topic.number_of_attempted_questions = 0
        topic.number_of_success_first_attempt = 0
        topic.number_of_latest_success_attempt = 0
        topic.number_of_attempted_open_questions = 0
        topic.avg_first_self_rated_score = 0.0
        topic.avg_latest_self_rated_score = 0.0
        topic.save()
    for topic in ScienceLevel3Topic.objects.all():
        topic.number_of_questions = 0
        topic.number_of_attempted_questions = 0
        topic.number_of_success_first_attempt = 0
        topic.number_of_latest_success_attempt = 0
        topic.number_of_attempted_open_questions = 0
        topic.avg_first_self_rated_score = 0.0
        topic.avg_latest_self_rated_score = 0.0
        topic.save()

    for q in ScienceQuestion.objects.all():
        topiclist = q.topic_number.split(";")
        subtopiclist = q.subtopic_number.split(";")
        level3topiclist = q.lv3_topic_number.split(";")
        if(q.question_subject == "Science" and q.question_type == "MCQ"):
            for topic in ScienceTopic.objects.all():
                #print("Topic level 1: ", topic.topic_index)
                for t in topiclist:
                    #print ("t = ", t)
                    if t == topic.topic_index:
                        #print("Match!")
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                        if q.success_on_first_attempt == "Yes":
                            topic.number_of_success_first_attempt = topic.number_of_success_first_attempt + 1
                            if q.number_of_attempts == 1 and q.last_attempt_success == "No":
                                q.last_attempt_success = "Yes"
                                q.save()
                        if q.last_attempt_success == "Yes":
                            topic.number_of_latest_success_attempt = topic.number_of_latest_success_attempt + 1

                        topic.save()
            for topic in ScienceSubTopic.objects.all():
                #print("Topic level 2: ", topic.topic_index)
                for t in subtopiclist:
                    #print("level 2 t = ", t)
                    if t == topic.topic_index:
                        #print("Match!")
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                        if q.success_on_first_attempt == "Yes":
                            topic.number_of_success_first_attempt = topic.number_of_success_first_attempt + 1
                            if q.number_of_attempts == 1 and q.last_attempt_success == "No":
                                q.last_attempt_success = "Yes"
                                q.save()
                        if q.last_attempt_success == "Yes":
                            topic.number_of_latest_success_attempt = topic.number_of_latest_success_attempt + 1
                        topic.save()
            for topic in ScienceLevel3Topic.objects.all():
                for t in level3topiclist:
                    #print("level 3 t = ", t)
                    if t == topic.topic_index:
                        #print ("Match! ", t)
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                        if q.success_on_first_attempt == "Yes":
                            topic.number_of_success_first_attempt = topic.number_of_success_first_attempt + 1
                            if q.number_of_attempts == 1 and q.last_attempt_success == "No":
                                q.last_attempt_success = "Yes"
                                q.save()
                        if q.last_attempt_success == "Yes":
                            topic.number_of_latest_success_attempt = topic.number_of_latest_success_attempt + 1
                        topic.save()
        #print("before search for open")
        if (q.question_subject == "Science" and q.question_type == "Open"):
           # print("search for Open questions")
            for topic in ScienceTopic.objects.all():
                # print("Topic level 1: ", topic.topic_index)
                for t in topiclist:
                    #print ("t = ", t)
                    if t == topic.topic_index:
                        #print("Match!")
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                            if(q.number_of_attempts == 1):
                                topic.avg_first_self_rated_score = (topic.avg_first_self_rated_score * topic.number_of_attempted_open_questions + q.first_self_rated_score)/(topic.number_of_attempted_open_questions + 1)
                            topic.avg_latest_self_rated_score = (topic.avg_latest_self_rated_score * topic.number_of_attempted_open_questions + q.latest_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.number_of_attempted_open_questions = topic.number_of_attempted_open_questions + 1
                        topic.save()
            for topic in ScienceSubTopic.objects.all():
                # print("Topic level 2: ", topic.topic_index)
                for t in subtopiclist:
                    # print("level 2 t = ", t)
                    if t == topic.topic_index:
                        # print("Match!")
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                            if (q.number_of_attempts == 1):
                                topic.avg_first_self_rated_score = (topic.avg_first_self_rated_score * topic.number_of_attempted_open_questions + q.first_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.avg_latest_self_rated_score = (topic.avg_latest_self_rated_score * topic.number_of_attempted_open_questions + q.latest_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.number_of_attempted_open_questions = topic.number_of_attempted_open_questions + 1
                        topic.save()
            for topic in ScienceLevel3Topic.objects.all():
                for t in level3topiclist:
                    # print("level 3 t = ", t)
                    if t == topic.topic_index:
                        # print ("Match! ", t)
                        topic.number_of_questions = topic.number_of_questions + 1
                        if q.number_of_attempts > 0:
                            topic.number_of_attempted_questions = topic.number_of_attempted_questions + 1
                            if (q.number_of_attempts == 1):
                                topic.avg_first_self_rated_score = (topic.avg_first_self_rated_score * topic.number_of_attempted_open_questions + q.first_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.avg_latest_self_rated_score = (topic.avg_latest_self_rated_score * topic.number_of_attempted_open_questions + q.latest_self_rated_score) / (topic.number_of_attempted_open_questions + 1)
                            topic.number_of_attempted_open_questions = topic.number_of_attempted_open_questions + 1
                        topic.save()

    #delete all existing report instances first


    return HttpResponseRedirect(reverse('science:english_reportresult', args=()))
class EnglishReportresultView(generic.ListView):
    template_name = 'science/english_reportresult.html'
    context_object_name = 'level1_topic_list'

    print (datetime.datetime.now())

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ScienceTopic.objects.all()
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['level2_topic_list'] = ScienceSubTopic.objects.all()
        context_data['level3_topic_list'] = ScienceLevel3Topic.objects.all()
        return context_data


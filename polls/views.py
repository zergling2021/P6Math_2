from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
#from .models import Question
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from .forms import ReceiveAnswer
from fractions import Fraction

import random

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


from django.shortcuts import render

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5000]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

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
        if(obj.question_model_index == "Model 1"):
            print("model is 1")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_1(obj)
            obj.save()
        if (obj.question_model_index == "Model 2"):
            print("model is 2")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_2(obj)
            obj.save()
        if (obj.question_model_index == "Model 3"):
            print("model is 3")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_3(obj)
            obj.save()
        if (obj.question_model_index == "Model 4"):
            print("model is 4")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_4(obj)
            obj.save()
        if (obj.question_model_index == "Model 5"):
            print("model is 5")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_5(obj)
            obj.save()
        if (obj.question_model_index == "Model 6"):
            print("model is 6")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_6(obj)
            obj.save()
        if (obj.question_model_index == "Model 7"):
            print("model is 7")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_7(obj)
            obj.save()
        if (obj.question_model_index == "Model 8"):
            print("model is 8")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_8(obj)
            obj.save()
        if (obj.question_model_index == "Model 9"):
            print("model is 9")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_9(obj)
            obj.save()
        if (obj.question_model_index == "Model 10"):
            print("model is 10")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_10(obj)
            obj.save()
        if (obj.question_model_index == "Model 11"):
            print("model is 11")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_11(obj)
            obj.save()
        if (obj.question_model_index == "Model 12"):
            print("model is 12")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_12(obj)
            obj.save()
        if (obj.question_model_index == "Model 13"):
            print("model is 13")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_13(obj)
            obj.save()
        if (obj.question_model_index == "Model 14"):
            print("model is 14")
            obj.question_text, obj.correct_answer_a, obj.correct_answer_b, obj.correct_answer_c = fill_model_14(obj)
            obj.save()
        return obj

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """

        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        #selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        #selected_choice.answer = request.POST.get('answer', 'FFF')
        #selected_choice.answer = request.POST['answer']


        attempted_answer_a = request.POST['attempted_answer_a']
        if attempted_answer_a == '':
            attempted_answer_a = '0'
        attempted_answer_b = request.POST['attempted_answer_b']
        if attempted_answer_b == '':
            attempted_answer_b = '0'
        attempted_answer_c = request.POST['attempted_answer_c']
        if attempted_answer_c == '':
            attempted_answer_c = '0'

        if (float(question.correct_answer_a) == float(attempted_answer_a) and float(question.correct_answer_b) == float(attempted_answer_b) and float(question.correct_answer_c) == float(attempted_answer_c)):
        #if question.correct_answer_a == attempted_answer_a and question.correct_answer_b == attempted_answer_b and question.correct_answer_c == attempted_answer_c:
            question.result_text = "Your answer is correct!"
        else:
            question.result_text = "Your answer is wrong. Correct answer is " + "a) = " + question.correct_answer_a + " b) = " + question.correct_answer_b + " c) = " + question.correct_answer_c + "."

        question.save()

        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def fill_name1():
    Names = ["Alice", "April", "Aaron", "Abriel", "Adam", "Ben", "Blair", "Blake", "Camus", "Derek", "Elaine", "Frank"]
    return (Names[random.randint(0,10)])

def fill_name2():
    Names = ["Fred", "Forrest", "Fuller", "Franklin", "Judy", "George", "Gibbon", "Edward", "Eric", "Gilbert", "Gru", "Gary"]
    return (Names[random.randint(0, 10)])
def fill_name3():
    Names = ["Gartner", "Henry", "Harry", "Helen", "James", "Brandon", "Cadence", "Yumi", "Jane", "Chris", "Tony", "Ron"]
    return (Names[random.randint(0, 10)])
def fill_name4():
    Names = ["Amelie", "Brian", "Dawei", "Peter", "Devi", "Dan", "Betty", "Anne", "Vivian", "Petra", "Nicol", "Diana"]
    return (Names[random.randint(0, 10)])

def fill_item1():
    Items =["apple(s)", "pear(s)", "bead(s)", "book(s)", "marble(s)", "orange(s)", "egg(s)", "highlighter(s)"]
    return (Items[random.randint(0,7)])
def fill_item2():
    Items =["card(s)", "box(es)", "spoon(s)", "cup(s)", "fork(s)", "key(s)", "pen(s)", "seeds(s)"]
    return (Items[random.randint(0,7)])
def fill_color1():
    Items = ["red", "blue", "green"]
    return (Items[random.randint(0,2)])
def fill_color2():
    Items = ["orange", "pink", "brown"]
    return (Items[random.randint(0,2)])


def fill_model_1(question):

    z = random.randint(2,4)
    if(z == 2):
        x = random.randint(1,10)
        y = random.randint(1,10)
        b=3*y+x
        a=b+x
    if(z == 3):
        x = random.randint(1,5)*2
        y = random.randint(1,10)
        b = 2*y + x/2
        a = b+x
    if (z == 4):
        x = random.randint(1,5)*3
        y = random.randint(1,5)*3
        b = 5*y/3 + x/3
        a = b+x
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Name_2>", fill_name2())
    question_text = question_text.replace("<Name_3>", fill_name3())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Item_2>", fill_item2())
    #question_text = question_text.replace("<Item_3>", fill_item3())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))
    question_text = question_text.replace("<Number_Z>", str(z))
    question.correct_answer_a = str(b)


    print("new question text is " + question_text)
    print("correct answer is ", b)
    return question_text, b, 0, 0

def fill_model_2(question):

    n1 = -1
    for l in range(10000):
        x = random.randint(50,300)
        y = random.randint(2, 20)
        z = random.randint(1, y-1)
        fd1 = random.randint(2,30)
        fn1 = random.randint(1, fd1)

        print("l = ", l, " x = ", x, " y = ", y, " z = ", z, " fraction = ", fn1, "/", fd1)

        if((fn1/fd1)*y/z == 1):
            print("divide by zero!")
            continue
        n1 = (fn1/fd1)*x/(1-((fn1/fd1)*y/z))
        print("n1 = ", n1)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer = str(n1)
            break
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Name_2>", fill_name2())
    question_text = question_text.replace("<Name_3>", fill_name3())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Item_2>", fill_item2())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))
    question_text = question_text.replace("<Number_Z>", str(z))
    question_text = question_text.replace("<Fraction_1_Numberator>", str(fn1))
    question_text = question_text.replace("<Fraction_1_Demoninator>", str(fd1))
    question.correct_answer = str(n1)
    print("new question text is " + question_text)

    return question_text, n1, 0, 0


def fill_model_3(question):

    n1 = -1
    n2 = -1
    for l in range(10000):
        x = random.randint(50,300)
        y = random.randint(2, 30)
        p1 = random.randint(1,3)/10
        p2 = random.randint(1,5)/10

        print("l = ", l, " x = ", x, " y = ", y, " p1 = ", p1, " p2= ", p2)

        n1 = (x-y)/(1-2*p1)
        n2 = round((p1+p2)/(1+p2), 2)
        print("n1 = ", n1)
        print("n2 = ", n2)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer_a = str(n1)
            question.correct_answer_b = str(n2)
            break
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Name_2>", fill_name2())
    question_text = question_text.replace("<Name_3>", fill_name3())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Item_2>", fill_item2())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))
    question_text = question_text.replace("<Percentage_1>", str(p1*100) + "%")
    question_text = question_text.replace("<Percentage_2>", str(p2*100) + "%")
    print("new question text of model 3 is " + question_text)

    return question_text, n1, n2, 0

def fill_model_4(question):

    n1 = -1
    n2 = -1
    for l in range(10000):
        x = random.randint(50,300)
        y = random.randint(2, 10)
        fd1 = random.randint(2, 10)
        fn1 = random.randint(1, fd1-1)
        fd2 = random.randint(2, 10)
        fn2 = random.randint(1, fd2-1)
        fd3 = random.randint(2, 10)
        fn3 = random.randint(1, fd3-1)

        print("l = ", l)
        if(1-(fn1/fd1)-(fn2/fd2)+(fn3/fd3)*(fn1/fd1)) == 0:
            continue
        n1 = (fn1/fd1)*(fn3/fd3)*x/(1-(fn1/fd1)-(fn2/fd2)+(fn3/fd3)*(fn1/fd1))
        print("n1 = ", n1)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer_a = str(n1)
            break
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Name_2>", fill_name2())
    question_text = question_text.replace("<Name_3>", fill_name3())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Item_2>", fill_item2())
    question_text = question_text.replace("<Color_1>", fill_color1())
    question_text = question_text.replace("<Color_2>", fill_color2())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))
    question_text = question_text.replace("<Fraction_1_Numberator>", str(fn1))
    question_text = question_text.replace("<Fraction_1_Demoninator>", str(fd1))
    question_text = question_text.replace("<Fraction_2_Numberator>", str(fn2))
    question_text = question_text.replace("<Fraction_2_Demoninator>", str(fd2))
    question_text = question_text.replace("<Fraction_3_Numberator>", str(fn3))
    question_text = question_text.replace("<Fraction_3_Demoninator>", str(fd3))
    print("new question text of model 4 is " + question_text)

    return question_text, n1, 0, 0


def fill_model_5(question):

    n1 = -1
    n2 = -1
    for l in range(10000):
        x = random.randint(10, 30)*3
        y = random.randint(2, 100)
        z = random.randint(3, 10)
        w = random.randint(3, 10)
        v = random.randint(2, 100)



        print("l = ", l)
        n1 = v*(x/3)+v*z-y
        n2 = n1 + (v*x/3) - w*v
        print("n1 = ", n1, " n2 = ", n2)
        if(n1 < 1000 and n1.is_integer() and n1 > 0 and n2.is_integer() and n2>0):
            break
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Name_2>", fill_name2())
    question_text = question_text.replace("<Name_3>", fill_name3())
    question_text = question_text.replace("<Name_4>", fill_name4())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Item_2>", fill_item2())
    question_text = question_text.replace("<Color_1>", fill_color1())
    question_text = question_text.replace("<Color_2>", fill_color2())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))
    question_text = question_text.replace("<Number_Z>", str(z))
    question_text = question_text.replace("<Number_W>", str(w))
    question_text = question_text.replace("<Number_V>", str(v))
    print("new question text of model 5 is " + question_text)

    return question_text, n1, n2, 0

def fill_model_6(question):

    n1 = -1
    n2 = -1
    for l in range(10000):
        x = random.randint(50,300)
        h = round((random.randint(5000, 30000))/100,2)
        i = round((random.randint(5000, 30000))/100,2)
        p1 = random.randint(1,50)/100
        p2 = random.randint(1,50)/100

        print("l = ", l)
        n1 = h/(1-p1)
        n2 = round(100*(i-(h*p1/(1-p1)))/((i-(h*p1/(1-p1))) + x), 2)
        print("n1 = ", n1)
        print("n2 = ", n2)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer_a = str(n1)
            question.correct_answer_b = str(n2)
            break
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Name_2>", fill_name2())
    question_text = question_text.replace("<Name_3>", fill_name3())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Item_2>", fill_item2())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Float_H>", str(h))
    question_text = question_text.replace("<Float_I>", str(i))


    question_text = question_text.replace("<Percentage_1>", str(p1*100) + "%")
    question_text = question_text.replace("<Percentage_2>", str(p2*100) + "%")
    print("new question text of is " + question_text)

    return question_text, n1, n2, 0

def fill_model_7(question):

    n1 = -1
    n2 = -1
    for l in range(10000):
        x = random.randint(50,300)
        y = random.randint(50, 300)
        fd1 = random.randint(2, 10)
        fn1 = random.randint(1, fd1-1)
        fd2 = random.randint(2, 10)
        fn2 = random.randint(1, fd2-1)

        if fn2/fd2 <= fn1/fd1:
            continue

        print("l = ", l)
        n1 = 2*(y - (1-fn1/fd1)*x)/(fn2/fd2 - fn1/fd1) + x
        print("n1 = ", n1)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer_a = str(n1)
            break
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Name_2>", fill_name2())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))
    question_text = question_text.replace("<Fraction_1_Numberator>", str(fn1))
    question_text = question_text.replace("<Fraction_1_Demoninator>", str(fd1))
    question_text = question_text.replace("<Fraction_2_Numberator>", str(fn2))
    question_text = question_text.replace("<Fraction_2_Demoninator>", str(fd2))
    print("new question text is " + question_text)

    return question_text, n1, 0, 0

def fill_model_8(question):

    n1 = -1
    n2 = -1
    for l in range(10000):
        x = random.randint(50,500)
        y = random.randint(5, 10)
        z = random.randint(2, 4)
        u = random.randint(10, 30)


        print("l = ", l)
        n1 = (2 * x - u * z + u * y) / (y + z)
        print("n1 = ", n1)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer_a = str(n1)
            break
    question_text = question.question_model

    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))
    question_text = question_text.replace("<Number_Z>", str(z))
    question_text = question_text.replace("<Number_U>", str(u))

    print("new question text is " + question_text)

    return question_text, n1, 0, 0

def fill_model_9(question):

    n1 = -1
    n2 = -1
    for l in range(10000):
        x = random.randint(50,300)
        y = random.randint(50, 200)
        z = random.randint(10, 30)


        print("l = ", l)
        print("z ", z, " y ", y, "(100*z)%y ", (100*z)%y)
        if (x/((100*z)//y)).is_integer():
            n1 = x/((100*z)//y)
        else:
            n1 = (x/((100*z)//y)+1)//1
        print("n1 = ", n1)
        if n1 > 0:
            question.correct_answer_a = str(n1)
            break
    question_text = question.question_model

    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))
    question_text = question_text.replace("<Number_Z>", str(z))


    print("new question text is " + question_text)

    return question_text, n1, 0, 0

def fill_model_10(question):

    n1 = -1
    n2 = -1
    for l in range(10000):
        h = round((random.randint(1000, 10000)) / 100, 2)
        i = round((random.randint(1000, 10000)) / 100, 2)
        p1 = random.randint(10, 30) / 100
        p2 = random.randint(10, 50) / 100

        print("l = ", l)
        if p2 == p1:
            continue
        n1 = (h + i) / (p2 - p1)
        n2 = round((n1 * (1 - p2) + i), 2)

        print("n1 = ", n1, " n2 = ", n2)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer_a = str(n1)
            break
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Color_1>", fill_color1())
    question_text = question_text.replace("<Color_2>", fill_color2())
    question_text = question_text.replace("<Percentage_1>", str(p1 * 100) + "%")
    question_text = question_text.replace("<Percentage_2>", str(p2 * 100) + "%")
    question_text = question_text.replace("<Float_H>", str(h))
    question_text = question_text.replace("<Float_I>", str(i))
    print("new question text is " + question_text)

    return question_text, n1, n2, 0

def fill_model_11(question):

    n1 = -1
    n2 = -1
    for l in range(10000):

        x = random.randint(30, 50)
        y = random.randint(10, 20)
        fd1 = random.randint(2, 10)
        fn1 = random.randint(1, fd1 - 1)
        fd2 = random.randint(2, 10)
        fn2 = random.randint(1, fd2 - 1)

        if fn1/fd1 <= fn2/fd2:
            continue

        print("l = ", l)
        n1 = (1 - (fn2 / fd2)) * (x - y) / (fn1 / fd1 - fn2 / fd2)


        print("n1 = ", n1)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer_a = str(n1)
            break
    question_text = question.question_model
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))
    question_text = question_text.replace("<Fraction_1_Numberator>", str(fn1))
    question_text = question_text.replace("<Fraction_1_Demoninator>", str(fd1))
    question_text = question_text.replace("<Fraction_2_Numberator>", str(fn2))
    question_text = question_text.replace("<Fraction_2_Demoninator>", str(fd2))
    print("new question text is " + question_text)

    return question_text, n1, 0, 0

def fill_model_12(question):

    n1 = -1
    n2 = -1
    for l in range(10000):

        x = random.randint(30, 60)
        fd1 = random.randint(2, 10)
        fn1 = random.randint(1, fd1 - 1)
        fd2 = random.randint(2, 10)
        fn2 = random.randint(1, fd2 - 1)

        if (fn1/fd1 + fn2/fd2) > 0.9:
            continue

        print("l = ", l)
        n1 = x / (1 - fn1 / (fn1 + fd1) - 2 * fn2 / (fn2 + fd2))

        print("n1 = ", n1)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer_a = str(n1)
            break
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Name_2>", fill_name2())
    question_text = question_text.replace("<Name_3>", fill_name3())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Fraction_1_Numberator>", str(fn1))
    question_text = question_text.replace("<Fraction_1_Demoninator>", str(fd1))
    question_text = question_text.replace("<Fraction_2_Numberator>", str(fn2))
    question_text = question_text.replace("<Fraction_2_Demoninator>", str(fd2))
    print("new question text is " + question_text)

    return question_text, n1, 0, 0

def fill_model_13(question):

    n1 = -1
    n2 = -1
    for l in range(10000):

        x = random.randint(200, 600)
        p1 = round(random.randint(1, 50) / 100, 2)
        p2 = round(random.randint(1, 50) / 100, 2)
        p3 = round(random.randint(1, 50) / 100, 2)
        fd1 = random.randint(2, 10)
        fn1 = random.randint(1, fd1 - 1)

        print("l = ", l)
        n1 = p3 * x / ((1 + p3) * (fn1 * p1 / fd1 + p2))
        print("n1 = ", n1)
        if(n1 < 1000 and n1.is_integer() and n1 > 0):
            question.correct_answer_a = str(n1)
            break
    question_text = question.question_model

    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Fraction_1_Numberator>", str(fn1))
    question_text = question_text.replace("<Fraction_1_Demoninator>", str(fd1))
    question_text = question_text.replace("<Percentage_1>", str(round(p1 * 100, 0)) + "%")
    question_text = question_text.replace("<Percentage_2>", str(round(p2 * 100, 0)) + "%")
    question_text = question_text.replace("<Percentage_3>", str(round(p3 * 100, 0)) + "%")

    print("new question text is " + question_text)

    return question_text, n1, 0, 0

def fill_model_14(question):

    n1 = -1
    n2 = -1
    for l in range(10000):

        x = random.randint(15, 30)
        y = random.randint(1000, 3000)
        fd1 = random.randint(3, 10)
        fn1 = random.randint(1, fd1 - 1)
        fd2 = random.randint(3, 10)
        fn2 = random.randint(1, fd2 - 1)
        fd3 = random.randint(3, 10)
        fn3 = random.randint(1, fd3 - 1)

        print("l = ", l)
        n1 = y / ((fn3 * x / fd3) / (1 - fn3 / fd3) + fn1 * x / fd1)
        n2 = (x * (fn3 / fd3) * n1) / (1 - fn3 / fd3)
        print("n1 = ", n1, " n2 = ", n2)
        if n1 < 1000 and n1.is_integer() and n1 > 0 and n2.is_integer() and n2 > 0:
            question.correct_answer_a = str(n1)
            break
    question_text = question.question_model
    question_text = question_text.replace("<Name_1>", fill_name1())
    question_text = question_text.replace("<Item_1>", fill_item1())
    question_text = question_text.replace("<Item_2>", fill_item2())
    question_text = question_text.replace("<Number_X>", str(x))
    question_text = question_text.replace("<Number_Y>", str(y))

    question_text = question_text.replace("<Fraction_1_Numberator>", str(fn1))
    question_text = question_text.replace("<Fraction_1_Demoninator>", str(fd1))
    question_text = question_text.replace("<Fraction_2_Numberator>", str(fn2))
    question_text = question_text.replace("<Fraction_2_Demoninator>", str(fd2))
    question_text = question_text.replace("<Fraction_3_Numberator>", str(fn3))
    question_text = question_text.replace("<Fraction_3_Demoninator>", str(fd3))

    print("new question text is " + question_text)

    return question_text, n1, n2, 0

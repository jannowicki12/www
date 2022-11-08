from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

def home(request):
    return render(template_name='polls/home.html', request=request)

def get_question_list(request):
    question = Question.objects.all()
    context = {
        "question": question
    }
    return render(template_name='polls/question_list.html', request=request, context=context)

def get_question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        "question": question
    }
    return render(template_name='polls/question_detail.html', request=request, context=context)


from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import QuestionForm, ChoiceForm

def question_add(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuestionForm()
    return render(request, 'polls/question_form.html', {'form': form})


def choice_add(request):
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('question_list'))
    else:
        form = ChoiceForm()
    return render(request, 'polls/choice_form.html', {"form": form}) 
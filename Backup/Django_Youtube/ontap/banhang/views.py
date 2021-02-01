from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Question
# Create your views here.
def index(request):
    return HttpResponse('Hello world!')

def QuestionPage(request):
    questions_list = Question.objects.all()
    context = {'qs':questions_list}
    return render(request, ('banhang/question-page.html'), context)


    
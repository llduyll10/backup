from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

#Fucntion base View
def index(request):
    myname='DuyNND'
    item = ['Macbook', 'iPhone', 'EXCITER','handsome']
    context={"name":myname, "items":item}
    return render(request,('polls/index.html'),context)

def viewListQuestion(request):
    list_questions = Question.objects.all()
    # list_questions = get_object_or_404(Question,pk=5)
    context = {'list_request': list_questions}
    return render(request, ('polls/question_list.html'),context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    context = {'qs':q}
    return render(request,('polls/detail_question.html'),context)

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    # Lay param tren url
    try:
        data = request.POST['choice']
        c = q.choice_set.get(pk=data)
    except:
        return HttpResponse("Error")
    c.vote = c.vote + 1
    c.save()
    context = {'q':q}
    return render(request, ('polls/result.html'), context)
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.

#Class base view
class IndexClass(View):
    def get(self, request):
        return HttpResponse('hello world!')

class SaveNewClass(View):
    def get(self, request):
        a = PostForm()
        return render(request,('news/add-news.html'),{'f':a})

    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('SAVE SUCCESS')
        else:
            return HttpResponse('Form is not valid')

class EmailViewClass(View):
    def get(self, request):
        b = SendEmail()
        return render(request, ('news/email.html'),{'f':b})

class ProcessClass(View):
    def post(self, request):
        g = SendEmail(request.POST)
        if g.is_valid():
            title = g.cleaned_data['title']
            content = g.cleaned_data['content']
            cc = g.cleaned_data['cc']
            email = g.cleaned_data['email']
            context = {
                'title':title,
                'content':content,
                'cc':cc,
                'email':email,
            }
            return render(request,('news/print-email.html'),context)
        else:
            return HttpResponse('Form not validate')

    
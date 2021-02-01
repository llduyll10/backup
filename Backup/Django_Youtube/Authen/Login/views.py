from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
# Create your views here.

class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>Login</h1>')

class LoginClass(View):
    def get(self, request):
        return render(request, ('Login/login.html'))

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        my_user = authenticate(username=username, password=password)
        if my_user is None:
            return HttpResponse('User not exist!')

        login(request,my_user)
        return render(request,('Login/success.html'))

class ViewUserAuthen(LoginRequiredMixin,View):
    login_url='/login/login'
    def get(self,request):
        return HttpResponse('<h1>This is my page of you</h1>')
    
@decorators.login_required(login_url='/login/login')
def view_product(request):
    return HttpResponse('View product')


class AddPost(LoginRequiredMixin, View):
    login_url='/login/login'

    def get(self, request):
        f = PostForm
        context = {'fm':f}
        return render(request,('Login/add-post.html'),context)

    def post(self, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('Form not valid')
        
        if request.user.has_perm('Login.add_post'):
            f.save()
        else:
            return HttpResponse('You not have permisson')

        return HttpResponse('ADD POST OK')
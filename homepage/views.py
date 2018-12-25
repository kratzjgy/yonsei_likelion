from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Homepage
from .models import Post
from .models import Comment
#from .models import .
from .forms import CommentForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.template import loader

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'homepage/register.html', {'form' : form})
def index(request):
    template = loader.get_template('homepage/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request,'homepage/about.html',{}) 

def post(request):
    post_list = Post.objects.all()
    return render(request, 'homepage/post.html', {
        'post_list': post_list,
    })
    
def post_detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'homepage/post_detail.html', {
        'post': post,
    })
    
def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('homepage.views.post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'homepage/post_form.html', {
        'form' : form,
    })
        
def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('homepage.views.post_detail', post_pk)
    else:
        form = CommentForm(instance = comment)
    return render(request, 'homepage/post_form.html', {
        'form' : form,
    })
    
def home(request):
    return render(request,'homepage/home.html',{}) 

from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
#MODEL IMPORT
from .models import Homepage
from .models import Post
from .models import Comment
#FORM IMPORT
from .forms import CommentForm
from .forms import PostForm
from .forms import SearchForm
from .forms import UserRegistrationForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import loader


#LOGIN
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

#INDEX
def index(request):
    template = loader.get_template('homepage/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request,'homepage/about.html',{}) 

#POST

def post(request):
    post_list = Post.objects.all().order_by('id')
    totalCnt = Post.objects.all().count()
    
    return render(request, 'homepage/post.html', {
        'post_list': post_list, 'totalCnt' : totalCnt, 
    })
###########################ERROR...#################################
def get_queryset(self):
    qs = Post.Objects.all()
    q = self.request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
        return qs
############################################################
def post_detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'homepage/post_detail.html', {
        'post': post,
    })
    
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('/post')
    else:
        form=PostForm()
    return render(request, 'homepage/post_form.html', {
        'form' : form
    })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            #post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('homepage.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'homepage/post_form.html', {
        'form': form,
    })
        
    
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('homepage.views.post')
    

#COMMENT

def comment_new(request, pk):
    #comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('homepage.views.post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'homepage/comment_form.html', {
        'form' : form,
    })
        
def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('homepage.views.post_detail', post_pk)
    else:
        form = CommentForm(instance = comment)
    return render(request, 'homepage/comment_form.html', {
        'form' : form,
    })
    
def comment_remove(request, post_pk, pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('homepage.views.post_detail', post_pk)
    
def home(request):
    return render(request,'homepage/home.html',{}) 

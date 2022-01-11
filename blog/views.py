from django.http import request
from django.shortcuts import render, redirect
from .models import Article, Review
from .forms import ArticleForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ArticleForm



def blogs(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'blogs.html', context)

def blog(request, id):
    article = Article.objects.get(id=id)
    context = {'article':article}
    return render(request, 'blog.html',context)

@login_required
def createArticle(request):
    # form = ArticleForm()
    # context= {
    #     'form': form
    # }
    # if request.method == "POST":
        
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     Article.objects.create(title=title, content=content)
    #     context['title'] = title
    #     context['content'] = content
    #     context = {'title':title, 'content':content}

    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')   
    context = {'form':form}
    return render(request, 'article_form.html', context) 

def updateArticle(request, id):
    
    article = Article.objects.get(id=id)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('blogs') 

    return render(request,'article_form.html',{'form':form,'article':article}) 

def deleteArticle(request, id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        article.delete()
        return redirect('blogs')
    context = {'obj':article}

    return render(request, 'delete.html', context) 

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    return render(request, 'login_register.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('blogs')
    return render(request, 'logout.html')

def register_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form_obj = form.save()
        return redirect('/login')
    context = {'form':form}    
    return render(request, 'register.html', context)    


    return render(request, 'login.html',)    

# def search_view(request):
#     search_d = request.GET
#     search = search_d.get("s")
#     article = None
#     if search is not None:
#         article = Article.objects.get()
    
#     context = {'article':article}
#     return render(request, 'search.html', context)
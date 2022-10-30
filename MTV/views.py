from contextlib import redirect_stderr
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm
# Create your views here.
def home(request) : 
    posts = Blog.objects.filter().order_by('-date') #블로그에 만든 객체 가져오기 
    
    return render(request, 'MTV/index.html', {'posts':posts})

def new(request) : 
    return render(request, 'MTV/new.html')

def create(request) : 
    if(request.method == 'POST'): 
        post = Blog() # 블로그 객체 생성
        post.title = request.POST['title']  # 객체 안에 post방식으로 타이틀 담고 바디 담고 시간 담기
        post.body = request.POST['body'] 
        post.date = timezone.now()
        post.save() # 다 담았으면 저장하기 
    return redirect('home') # 다 끝나면 홈으로 리다이렉트 시킨다 

def formcreate(request):
    if request.method == 'POST': 
        form = BlogForm(request.POST) #form안에 아까 폼즈.py에서 만든 내용을 집어 넣는다 post로
        if form.is_valid():# 필드값이 잘 들어왔는지 확인 하는 코드 유효성 검사 
            post = Blog() # 우리가 정의한 블로그 형식으로 
            post.title = form.cleaned_data['title'] # 유효성 마친 데이터만  넣는다는 코드 
            post.body = form.cleaned_data['body']
            post.save() # 다 했으면 저장 
            return redirect('home') # 다끝나면 홈으로 리다이렉트 시킴 
    else:
        form = BlogForm()
    return render(request, 'MTV/form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES': 
        form = BlogModelForm(request.POST, request.FILES) #form안에 아까 폼즈.py에서 만든 내용을 집어 넣는다 post로
        if form.is_valid():# 필드값이 잘 들어왔는지 확인 하는 코드 유효성 검사                        
            form.save() # 다 했으면 저장 
            return redirect('home') # 다끝나면 홈으로 리다이렉트 시킴 
    else:
        form = BlogModelForm()
    return render(request, 'MTV/form_create.html', {'form':form})

def detail(request, blog_id):
    #blog_id 번째의 글을 데이터베이스로 부터 가져와서 뛰워 주는 코드
    blog_detail = get_object_or_404(Blog, pk=blog_id) 
    return render(request, 'MTV/detail.html', {'blog_detail':blog_detail})
#삭제 기능 
def delete(request, blog_id):    
     delete_date = get_object_or_404(Blog, id=blog_id)
     delete_date.delete()
     return redirect('home')
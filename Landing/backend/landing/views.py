from django.shortcuts import render, redirect
from landing.models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.views.generic.list import ListView
from .forms import PostForm
from django.core.paginator import Paginator

class AddPostView(ListView):
    model = News
    def get(self, request):
        form = PostForm()
        context = {
        'page': 'newsForm',
        'form': form
        }
        return render(request, 'newsForm.html', context)
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            descriptions = form.cleaned_data['descriptions']
            image = form.cleaned_data['image']
            news = News.objects.create(
                    title=title,
                    descriptions=descriptions,
                    image=image,
                    )
            news.save()
            messages.info(request,'+Add News, Successful !')
            return redirect('/news')
        return redirect('/newsForm')

def recentJob(request):
    data = JobOpportunities.objects.all().order_by('-created')
    print(data)
    context = {
        'jobs':data,
        'page': 'job'
    }
    return render(request,'recentJob.html', context)

def jobProfile(request):
    if request.user.is_authenticated:
        current_user = request.user
        data = JobOpportunities.objects.filter(user=current_user).order_by('-created')
        context = {
            'job_edit' : data,
            'page': 'job'
        }
        return render(request,'jobProfile.html', context)
    else:
        return redirect('/loginForm') 

def postJob(request):
    obj_user=request.user
    print(obj_user)
    # print("ID pk User")
    # print(get_user_id)
    # obj_user=User.objects.get(id=get_user_id)
    # print("Object User")
    # print(get_user)
    company=request.POST['company']
    job_position=request.POST['job_position']
    job_desc=request.POST['job_desc']
    email=request.POST['email']
    link=request.POST['link']

    if company == "" or job_position == "" or job_desc =="" or email =="" or link=="" :
        messages.info(request,f'Please fill down correctly and completely.')
        return redirect('/profile')
    else:    
        addJob = JobOpportunities.objects.create(
                user=obj_user,
                title=job_position,
                company=company,
                email=email,
                link=link,
                descriptions=job_desc,
                )
        addJob.save()
        messages.info(request,'Post Job Successful !')
        return redirect('/profile')
def index(request):
    data = News.objects.all().order_by('-created')[:4]
    context = {
        'newss':data,
        'page': 'index'
    }
    return render(request,'index.html', context)

def news(request):
    data = News.objects.all().order_by('-created')
    get_data = data[1:]
    context = {
        'newss':get_data,
        'last_news': News.objects.all().order_by('-created').first(),
        'page': 'news',

    }
    return render(request,'news.html', context)    

def newsAll(request):
    data = News.objects.all().order_by('-created')
    get_data = data
    p = Paginator(get_data, 4)
    page = request.GET.get('page')
    news_page = p.get_page(page)
    context = {
        # 'newss':get_data,
        'page': 'news',
        'news_page' : news_page,

    }  

    return render(request,'newsAll.html',context)

def newsDetail(request, id):
    data = News.objects.get(id=id)
    news={'news':data}
    return render(request,'newsDetail.html', news)

# def newsForm(request):
#     context = {
#         'page': 'newsForm'
#     }
#     if request.user.is_superuser:
#         return render(request,'newsForm.html', context)
#     elif request.user.is_authenticated:
#         messages.info(request,'The user does not have permission.')
#         return redirect('/')
#     else :
#         messages.info(request,'The user does not have permission.')
#         return redirect('/')
def loginForm(request):
    context = {
        'page': 'loginForm'
    }
    if request.user.is_authenticated or request.user.is_superuser:
        return redirect('/') 
    else:
        return render(request,'loginForm.html', context)

def log_out(request):
    logout(request)
    messages.info(request,'ออกจากระบบเรียบร้อย')
    return redirect('/') 

def knowledge(request):
    context = {
        'page': 'knowledge'
    }
    return render(request,'knowledge.html', context )

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    #check username
    user = auth.authenticate(username=username,password=password)
    print(user)
    if user is not None :
        auth.login(request,user)
        return redirect('/')  
    else:
        messages.info(request,'ไม่พบผู้ใช้งานในระบบ')
        return redirect('/loginForm') 

def registerForm(request):
    return render(request,'registerForm.html') 

def register(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if password == repassword :
        if username == "" or firstname == "" or lastname =="" or email =="" or password=="" or repassword=="" :
            messages.info(request,f'กรุณากรอกข้อมูลให้ครบทุกช่อง')
            return redirect('/registerForm')
        else:    
            if User.objects.filter(username=username).exists():
                messages.info(request,f'Username "{username}" นี้ถูกใช้งานแล้ว')
                return redirect('/registerForm')
            elif User.objects.filter(email=email).exists():
                messages.info(request,f'Email "{email}" นี้ถูกใช้งานแล้ว')
                return redirect('/registerForm')
            elif len(password) <= 7 :
                messages.info(request,f'Password ต้องมีตัวอักษรหรือตัวเลขอย่างน้อย 8 ตัว')
                return redirect('/registerForm') 
            else:
                user=User.objects.create(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname,
                )
                user.set_password(password)
                user.save()
                messages.info(request,'ลงทะเบียน เรียบร้อยแล้ว !')
                return redirect('/')
    else:
        messages.info(request,'Password ไม่ตรงกัน')
        return redirect('/registerForm')

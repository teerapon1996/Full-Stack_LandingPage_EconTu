from unicodedata import name
from django.urls import path, include # New
from django.views.generic import TemplateView # New
from landing import views


urlpatterns = [
    path('',views.index ,name='index'),
    path('news',views.news ,name='news'),
    path('newsAll',views.newsAll ,name='newsAll'),
    path('profile/',views.jobProfile ,name='jobProfile'),
    path('recentJob',views.recentJob ,name='recentJob'),
    path('profile/postJob',views.postJob ,name='postJob'),
    path('newsDetail/<int:id>', views.newsDetail,name='newsDetail'),
    path('newsForm/', views.AddPostView.as_view(), name='newsForm'),
    path('logout',views.log_out ,name='log_out'),
    path('login',views.login ,name='login'),
    path('loginForm',views.loginForm ,name='loginForm'),
    path('registerForm',views.registerForm ,name='registerForm'),
    path('register',views.register ,name='register'),
    path('knowledge',views.knowledge,name='knowledge'),
]
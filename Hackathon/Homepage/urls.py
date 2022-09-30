from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signupuser', views.signupuser, name='signupuser'),
    path('signupcompany', views.signupcompany, name='signupcompany'),
    path('company', views.company, name='company'),
    path('user', views.user, name='user'),
    path('jobinfo', views.jobinfo, name='jobinfo'),
    path('recommend', views.recommend, name='recommend'),
    path('checking', views.checking, name="checking"),
    path('verification', views.verification, name="verification"),
    path('freightmarket', views.freightmarket, name="freightmarket"),

    path('company-post-job/', views.postJob, name='company-post-job')
]
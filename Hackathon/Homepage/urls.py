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
    path('freightdisplay', views.freightdisplay, name="freightdisplay"),

    path('company-post-job/', views.postJob, name='company-post-job'),
    path('services', views.services, name='services'),
    path('railingRequest', views.railingRequest, name='railingRequest'),
    path('new_user', views.new_user, name='new_user'),

    path('stuffingRequest', views.stuffingRequest, name='stuffingRequest'),

    path('resources', views.resources, name='resources'),
    path('company-post-job/', views.postJob, name='company-post-job'),

    path('documentation', views.documentation, name='documentation'),

    path('truckingRequest', views.truckingRequest, name='truckingRequest'),
    path('forkliftServices', views.forkliftServices, name='forkliftServices'),


    path('home', views.home, name='home')
    
]
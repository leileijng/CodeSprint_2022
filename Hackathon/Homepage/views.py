from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import LoginForm, PostCoLoadingListing, UserSignupForm, CompanySignupForm, PostJobs, Verification
from django.views.decorators.csrf import csrf_exempt  
from .models import JobListing, Company, Individual, VerifiedJobListing, CoLoadingListing, VerifiedCoLoadingListing
import requests
import ssl
import json

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

  
# sending post request and saving response as response object
#r = requests.post(url = API_ENDPOINT, data = data)

def index(request):
    return render(request, 'index.html')


def login(request):
    msg = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if(form.is_valid()):
            #Payload = {
            #    "username": form.cleaned_data['Email'],
            #    "password": form.cleaned_data['Password']
            #}
            #r = requests.post(url = LOGIN, params = Payload, headers = API_KEY)
            #print(r)
            print(form.cleaned_data['Choice'])
            if(form.cleaned_data['Choice'] == '1'):
                for Data in Company.objects.all():
                    msg = 'Wrong Email/Password'
                return HttpResponseRedirect('home') 
            else:
                for Data in Individual.objects.all():
                    return HttpResponseRedirect('home')
                msg = 'Wrong Email/Password'
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form' : form, 'msg' : msg})

def signupuser(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if(form.is_valid()):
            #Payload = {
            #    "username": form.cleaned_data['Email'],
            #    "password": form.cleaned_data['Password']
            #}
            #r = requests.post(url = SIGNUP, params = Payload, headers = API_KEY)
            #print(r)
            form.save()
            return HttpResponseRedirect('login')
        else:
            print(form.errors)
    else:
        form = UserSignupForm()
        
    return render(request, 'individual_signup.html', {'form' : form})
Token = ""

def signupcompany(request):
    if request.method == 'POST':
        form = CompanySignupForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('login')
        else:
            print(form.errors)
    else:
        form = CompanySignupForm()
    return render(request, 'company_signup.html', {'form' : form})


def company(request):
    if request.method == 'POST':
        form = PostJobs(request.POST)
        if(form.is_valid()):
            form.save()
        else:
            print(form.errors)
    else:
        form = PostJobs()
        Verified = VerifiedCoLoadingListing.objects.all()
        NotVerified = CoLoadingListing.objects.all()
    return render(request, 'company.html', {'form' : form, 'Verified': Verified, 'NotVerified': NotVerified })

def verification(request):
    msg = ""
    if request.method == 'POST':
        form = Verification(request.POST)
        if(form.is_valid()):
            Payload = {
                "token": str(Token).replace('"',""),
                "confirmationCode": str(form.cleaned_data['VerificationCode'])
            }
            
            r = requests.post(url = SIGNUPCONFIRM, json = Payload, headers = API_KEY)
            print(form.cleaned_data['VerificationCode'])
            print(str(Token).replace('"',""))
            if(r.status_code == 200):
                return HttpResponseRedirect('checking')
            else:
                msg = 'Wrong Verification Code'
        else:
            print(form.errors) 
    else:
        form = Verification()
    return render(request, 'verification.html', {'form' : form, 'msg': msg})


def user(request):
    return render(request, 'user.html')

def freightmarket(request):
    if request.method == 'POST':
        form = PostCoLoadingListing(request.POST)
        if(form.is_valid()):
            form.save()
        else:
            print(form.errors)
    else:
        form = PostCoLoadingListing()
        Verified = VerifiedJobListing.objects.all()
        NotVerified = JobListing.objects.all()
    return render(request, 'freightmarket.html', {'form' : form, 'Verified': Verified, 'NotVerified': NotVerified })

def freightdisplay(request):
    return render(request, 'freightdisplay.html')

def resources(request):
    return render(request, 'resources.html')

def signup(request):
    return render(request, 'signup.html')

def jobinfo(request):
    return render(request, 'job_display.html')

def new_user(request):
    return render(request, 'new_user.html')

def recommend(request):
    return render(request, 'recommend.html')

def checking(request):
    return render(request, 'checking.html')

def postJob(request):
    if request.method == 'POST':
        response_json = request.POST
        response_json = json.dumps(response_json)
        data = json.loads(response_json)
        print(data)
    return HttpResponse("Posted Successfully")

def services(request):
    return render(request, 'services.html')

def railingRequest(request):
    return render(request, 'railingRequest.html')

def stuffingRequest(request):
    return render(request, 'stuffingRequest.html')

def documentation(request):
    return render(request, 'documentation.html')
def truckingRequest(request):
    return render(request, 'truckingRequest.html')

def forkliftServices(request):
    return render(request, 'forkliftServices.html')

def home(request):
    return render(request, 'home.html')

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from my_profile_feed.models import Skill, Interest, user_profile, Experience, Address, Education_details, Certifications
from profiles.models import Follow, Following, Follower
from .models import signup_model
from . import forms,models
from django.contrib.auth.models import User

username='/0'
def signin(request):
    if request.session.has_key('username'):
        return signin_a(request)
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        for record in User.objects.all():
            if record.email.upper()==username.upper() and check_password(password, record.password):
                signup_model.objects.filter(email=username).update(password=record.password)
                request.session['username']=username.lower()
                print(request.session['username'])
            
                return HttpResponseRedirect(reverse('index:index'))

    return signup(request)

def signin_a(request):
    if request.session.has_key('username'):
        return render(request,'signin_a.html')

def signup(request):
    username='/0'
    if request.method=='POST':
        print('HELLO')
        if request.session.has_key('username'):

            username= request.session['username']
            print(username)

        myform=forms.MyForm(data=request.POST)
        if myform.is_valid():
            full_name = myform.cleaned_data['full_name']
            phone = myform.cleaned_data['phone']
            email = myform.cleaned_data['email']
            password = myform.cleaned_data['password']
            repeat_password = myform.cleaned_data['repeat_password']
            if password == repeat_password:
                hashed_password = make_password(password)
                signup_model(full_name=full_name, phone=phone, email=email, password=hashed_password,
                            repeat_password=hashed_password).save()

                User(username=full_name, email=email, password=hashed_password).save()

                usr = user_profile(
                    user_name=myform.cleaned_data['full_name'],
                    user_email=myform.cleaned_data['email'],
                    overview="",
                    experience=[],
                    address=Address(locality="", city="", zip="", country=""),
                    skills=[],
                    interests=[],
                    education_details=[],
                    certifications=[],
                    notification = [],
                    follow_notification = [],
                    chats = [])

                usr.save()
                Follow(user_name = myform.cleaned_data['email'], follower=[], following=[]).save()
               

        return render(request,'signin.html',{'myform': myform,'username':username})

    else:
        myform=forms.MyForm()


    return render(request,'signin.html',{'myform': myform,'username':username})

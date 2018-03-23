# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    request.session.flush()
    return render(request, "log_reg_app/index.html")

def register(request):
    response = User.objects.register_validator(request.POST)
    print request.POST['bday']
    if response['status']:
        request.session['user_id'] = response['user'].id
        return redirect ('/quotes') 
    else:
        for tag, error in response['errors'].iteritems():
            messages.error(request, error, extra_tags="register")
        return redirect ('/')

def login(request):
    response = User.objects.login_validator(request.POST)

    if response['status']:
        request.session['user_id'] = response['user'].id
        return redirect ('/quotes')
    else:
        for tag, error in response['errors'].iteritems():
            messages.error(request, error, extra_tags='login')
        return redirect ('/')

def show(request, user_id):
    if not 'user_id' in request.session: #PUT THIS LINE IN EVERY RENDER PAGE
        return redirect('/')

    context = {
        'user': User.objects.get(id=user_id)
    }

    return render(request, "log_reg_app/user.html", context)
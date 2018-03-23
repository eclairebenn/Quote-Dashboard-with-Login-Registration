# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from ..log_reg_app.models import User
from .models import Quoter, Quote
from django.contrib import messages
import bcrypt

def home(request):
    if not 'user_id' in request.session:
        return redirect('/')
    quote_display = {}
    quotes = Quote.objects.all()
    user_favorites = User.objects.get(id=request.session['user_id']).favorited_quotes.all()
    for quote in quotes:
        match = user_favorites.filter(id=quote.id)
        if len(match) == 0:
            quote_display[quote.id] = quote
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'quotes' : quote_display,
        'user_favorites' : user_favorites
    }
    return render(request, 'quotes_app/home.html', context)

def create(request):
    user_id = request.session['user_id']
    response = Quote.objects.create_quote_validator(request.POST, user_id)
    
    if not response['status']:
        for tag, error in response['errors'].iteritems():
            messages.error(request, error)

    return redirect('/quotes')

def favorite(request, quote_id):
    u = User.objects.get(id=request.session['user_id'])
    q = Quote.objects.get(id=quote_id)
    new_favorite = u.favorited_quotes.add(q)
    return redirect('/quotes')

def unfavorite(request, quote_id):
    u = User.objects.get(id=request.session['user_id'])
    q = Quote.objects.get(id=quote_id)
    del_favorite = u.favorited_quotes.remove(q)
    return redirect('/quotes')




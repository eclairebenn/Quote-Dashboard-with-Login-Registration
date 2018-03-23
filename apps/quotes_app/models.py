# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..log_reg_app.models import User

class QuoteManager(models.Manager):
    def create_quote_validator(self, postData, user_id):
        result = {
            'status': False
        }
        errors = {}
        if len(postData['quoter']) < 4:
            errors['quoter_length'] = "The 'Quoted By' input must be longer than 3 characters"
        if len(postData['quote']) < 11:
            errors['quote_length'] = "The 'Message' input must be at least 11 characters"
        
        result['errors'] = errors
        if len(errors) == 0:
            result['status'] = True
            c = User.objects.get(id=user_id)
            q = Quoter.objects.create(name=postData['quoter'])
            new_quote = self.create(quoter=q, creator=c, content=postData['quote'])
        return result

class Quoter(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Quoter object: {}>".format(self.name)

class Quote(models.Model):
    content = models.TextField()
    quoter = models.ForeignKey(Quoter, related_name="quotes_said")
    creator = models.ForeignKey(User, related_name="quotes_created")
    favorited_users = models.ManyToManyField(User, related_name="favorited_quotes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    objects = QuoteManager()

    def __repr__(self):
        return "<Quote object: {}, {} {} {}>".format(self.content, self.quoter, self.creator, self.favorited_users)
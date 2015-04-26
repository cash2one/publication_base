# -*- coding: utf-8 -*-
'''
Created on May 24, 2013

@author: Sergey
'''
from django.contrib import admin
from model.models import Category, Category_Locale, Edition, Edition_Locale
from model.models import Issue, Rubric, Rubric_Locale
from model.models import Author, Author_Locale, Article, Article_Authors, Article_Locale

admin.site.register(Category)
admin.site.register(Category_Locale)
admin.site.register(Edition)
admin.site.register(Edition_Locale)
admin.site.register(Issue)
admin.site.register(Rubric)
admin.site.register(Rubric_Locale)
admin.site.register(Author)
admin.site.register(Author_Locale)
admin.site.register(Article)
admin.site.register(Article_Authors)
admin.site.register(Article_Locale)

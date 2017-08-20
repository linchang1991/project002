# -*- coding:utf-8 -*- 
from django import forms
from .models import Blog, Tag


class BlogForm(forms.Form):
	title = forms.CharField(required = True)
	author = forms.CharField(required = True, initial = "林畅")
	content = forms.CharField(required = True, widget = forms.Textarea(attrs = {"name":"editor1"}))
	tags = forms.ModelMultipleChoiceField(required = False, queryset = Tag.objects.all())
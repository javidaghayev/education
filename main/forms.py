from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Course, Blog, Subscriber, Comment


class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ['category', 'title', 'description', 'instructor']


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'content']


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'name', 'email']
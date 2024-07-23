from django.contrib import admin
from .models import Category, Course, Blog, Comment, Subscriber

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Subscriber)
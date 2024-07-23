from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Course, Blog, Subscriber, Comment
from .forms import CourseForm, BlogForm, SubscriberForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required



def course_list(request):
    courses = Course.objects.all().order_by('-id')
    context = {'courses': courses}
    return render(request, 'course.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}
    return render(request, 'course-single.html', context)







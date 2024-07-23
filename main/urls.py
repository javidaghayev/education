from django.urls import path
from main import views

urlpatterns = [
    path('', views.course_list, name='course-list')
]
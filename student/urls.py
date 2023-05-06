from django.urls import path
from student.views import student_view
urlpatterns = [
    path('',student_view),
]
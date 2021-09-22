from django.urls import path
from .views import *

urlpatterns = [
    path('', CoursesView.as_view(),name= 'courses'),
    path('<int:course_id>/', CoursesDetailView.as_view()),
]

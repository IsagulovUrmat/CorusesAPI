from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
    path('/courses', CourseView.as_view(), name='course-group'),
    path('/<int:course_id>/', CoursesDetailView.as_view()),
]

# router = DefaultRouter()
# router.register(r'', CourseView, basename='courses')
# urlpatterns = router.urls


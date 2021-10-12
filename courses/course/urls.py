from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
    path('courses/', CourseView.as_view(), name='courses'),
    path('courses/<int:course_id>/', CoursesDetailViewFirst.as_view(), name='course'),
]

# router = DefaultRouter()
# router.register(r'', CourseView, basename='courses')
# urlpatterns = router.urls


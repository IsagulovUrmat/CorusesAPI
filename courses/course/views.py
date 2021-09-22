from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import views, status
from .models import Category, Branch, Contact
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class CoursesView(views.APIView):

    def get(self, request, *args, **kwargs):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'OK'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class CoursesDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        doctor = Course.objects.get(id=kwargs['course_id'])
        serializer = CourseSerializer(doctor)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs['course_id'])
        course.delete()
        return Response({"data": "Delete successful!"})

class CategoryView(views.APIView):

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchView(views.APIView):

    def get(self, request, *args, **kwargs):
        branch = Branch.objects.all()
        serializer = CategorySerializer(branch, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactView(views.APIView):

    def get(self, request, *args, **kwargs):
        contact = Contact.objects.all()
        serializer = CategorySerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




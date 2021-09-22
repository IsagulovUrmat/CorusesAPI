from rest_framework import serializers, status
from rest_framework.response import Response

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'imgpath')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    contacts = ContactSerializer()
    branches = BranchSerializer()

    class Meta:
        model = Course
        fields = ['name', 'description', 'category', 'logo', 'contacts', 'branches']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        contacts_data = validated_data.pop('contacts')
        contacts = Contact.objects.create(**contacts_data)
        branches_data = validated_data.pop('branches')
        branches = Branch.objects.create(**branches_data)
        course = Course.objects.create(category=category, contacts=contacts, branches=branches, **validated_data)
        return course


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


# class CourseCreateSerializer(serializers.ModelSerializer):
#
#     category = CategorySerializer()
#     contacts = serializers.ListField(write_only=True)
#     branches = serializers.ListField(write_only=True)
#
#     class Meta:
#         model = Course
#         fields = ['name', 'description','logo', 'category', 'contacts', 'branches']
#
#     def create(self, validated_data):
#         category_data = validated_data.pop('category')
#         category = Category.objects.create(**category_data)
#         contacts_data = validated_data.pop('contacts')
#         # contacts = Contact.objects.create(**contacts_data)
#         branches_data = validated_data.pop('branches')
#         # branches = Branch.objects.create(**branches_data)
#         course = Course.objects.create(category=category, **validated_data)
#         for contact in contacts_data:
#             contact, created = Contact.objects.get_or_create(status=contact)
#             course.contacts.add(contact)
#         for branch in branches_data:
#             branch, created = Branch.objects.get_or_create(name=branch)
#             course.branches.add(branch)
#         return course


class NestedContactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'

class NestedBranchSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Branch
        fields = ('__all__')


class CourseGroupSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    contacts = NestedContactSerializer(many=True)
    branches = NestedBranchSerializer(many=True)

    class Meta:
        model = Course
        fields = ['name', 'description','logo', 'category', 'contacts', 'branches']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')
        courses = Course.objects.create(category=category, **validated_data)
        contacts_list = []  # it will contains list of Contact model instance
        branches_list = []
        for contact in contacts_data:
            contact_id = contact.pop('id', None)
            contact, _ = Contact.objects.get_or_create(id=contact_id, defaults=contact)
            contacts_list.append(contact)
        for branch in branches_data:
            branch_id = branch.pop('id', None)
            branch, _ = Branch.objects.get_or_create(id=branch_id, defaults=branch)
            branches_list.append(branch)
        # add all passed instances of contatcs, branches model to courses instance
        courses.contacts.add(*contacts_list)
        courses.branches.add(*branches_list)
        return courses




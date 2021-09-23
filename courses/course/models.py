from django.db import models

class Branch(models.Model):

    latitude = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    address = models.CharField(max_length=150)


    def __str__(self):
        return self.address

class Contact(models.Model):
    CHOICES = (
        (1,'Facebook'),
        (2,'Email'),
        (3, 'phone')
    )
    status = models.IntegerField(choices=CHOICES)


    def __str__(self):
        return f'{self.status}'

class Category(models.Model):
    name = models.CharField(max_length=150)
    imgpath = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Course(models.Model):

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', null=True)
    logo = models.CharField(max_length=150)
    contacts = models.ManyToManyField(Contact, related_name='contacts', null=True)
    branches = models.ManyToManyField(Branch, related_name='branches', null=True)

    def __str__(self):
        return self.name

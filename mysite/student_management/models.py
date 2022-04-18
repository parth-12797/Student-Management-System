from django.db import models

# Create your models here.
class Campus(models.Model):
    _id=models.IntegerField
    Campus_name=models.CharField(max_length=10)
    Campus_location=models.CharField(max_length=10)

    def __str__(self):
        return self.Campus_name

class Stream(models.Model):
    _id=models.IntegerField
    Stream_name=models.CharField(max_length=10)


    def __str__(self):
        return self.Stream_name


class Facility(models.Model):
    _id=models.IntegerField
    Facility_name=models.CharField(max_length=10)


    def __str__(self):
        return self.Facility_name


class Course(models.Model):
    _id=models.IntegerField
    Course_name=models.CharField(max_length=10)
    Stream_name=models.CharField(max_length=10)


    def __str__(self):
        return self.Course_name

class Lab(models.Model):
    _id=models.IntegerField

    lab_name=models.CharField(max_length=10)
    Course_name = models.CharField(max_length=10)


    def __str__(self):
        return self.lab_name

class Subject(models.Model):
    _id=models.IntegerField

    Subject_name=models.CharField(max_length=10)
    Course_name = models.CharField(max_length=10)


    def __str__(self):
        return self.Subject_name

class Faculty(models.Model):
    _id=models.IntegerField
    Faculty_name=models.TextField(max_length=25)
    Subject_name=models.CharField(max_length=10)
    Course_name = models.CharField(max_length=10)


    def __str__(self):
        return self.Faculty_name


class Students_data(models.Model):

    _id=models.IntegerField
    Student_name=models.TextField(max_length=25)
    Student_email=models.CharField(max_length=20)
    Course_name = models.CharField(max_length=10)
    Subjects = models.CharField(max_length=25)
    Labs=models.CharField(max_length=25)
    Facility=models.CharField(max_length=25)
    Stream=models.CharField(max_length=10)


    def __str__(self):
        return self.Student_name

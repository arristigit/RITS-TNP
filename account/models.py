from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    enrollment_no = models.CharField(max_length=250)
    institute = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    sem = models.IntegerField()
    year = models.IntegerField()
    contact = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    father_contact = models.CharField(max_length=250)
    signature = models.BooleanField(max_length=250)


class Company(models.Model):
    name = models.CharField(max_length=250)
    hr_name = models.CharField(max_length=250)
    designation_hr = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    board_no = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)


class Faculty(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    duration_allowed = models.IntegerField()
    allowed_from = models.DateField(auto_now=False, auto_now_add=False)
    allowed_till = models.DateField(auto_now=False, auto_now_add=False)
    date = models.DateTimeField(auto_now_add=True)


class Attendence(models.Model):
    student = models.OneToOneField("Student", on_delete=models.CASCADE)
    semester_1 = models.IntegerField()
    semester_2 = models.IntegerField()
    semester_3 = models.IntegerField()
    semester_4 = models.IntegerField()
    semester_5 = models.IntegerField()
    semester_6 = models.IntegerField()
    semester_7 = models.IntegerField()
    semester_8 = models.IntegerField()
from django.contrib import admin
from account.models import Student, Company, Faculty, Attendence

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Faculty)
admin.site.register(Attendence)
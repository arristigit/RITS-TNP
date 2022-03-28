from django.urls import path
from account.views import StudentView, FacultyView

urlpatterns = [
    path('student', StudentView.as_view(), name='student'),
    path('faculty', FacultyView.as_view(), name='faculty'),
]
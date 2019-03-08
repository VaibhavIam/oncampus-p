from django.urls import path
from faculty import views

urlpatterns = [
    path('', views.faculty_home, name='faculty_home'),
]
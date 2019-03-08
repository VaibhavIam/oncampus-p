from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required()
def faculty_home(request):
    return render(request, 'faculty/faculty_home.html')

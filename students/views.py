from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.


def home(request):
    if request.method == "POST":
            user = auth.authenticate(username=request.  POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                # 'student_home' for student
                return redirect('faculty_home')
            else:
                return render(request, 'students/home.html',{'error': 'Username or password is incorrect'})
    else:
        return render(request, 'students/home.html')


# @login_required()
def student_home(request):
    return render(request,'students/student_home.html')
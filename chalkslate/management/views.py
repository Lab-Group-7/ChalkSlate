from django.shortcuts import render
from . import forms

# def homepage(request):
#     return render(request, 'management/homepage.html', {})

def first_func(request):
    return render(request,'management/main.html', {})

def home(request):
    return render(request,'management/home.html')

def notice_board(request):
    return render(request,'management/notice-board.html')

def guide(request):
    return render(request,'management/guide.html')

def about_us(request):
    return render(request,'management/about-us.html')
def contact_us(request):
    return render(request,'management/contact-us.html')
def register(request):
    return render(request,'management/register.html')
def reg_admin(request):
    form = forms.AdminRegisterForm
    return render(request,'management/reg-admin.html', {'form' : form})
def reg_tutor(request):
    form = forms.TutorRegisterForm()
    return render(request,'management/reg-tutor.html', {'form' : form})

def reg_student(request):
    form = forms.StudentRegisterForm()
    return render(request,'management/reg-student.html', {'form' : form})

def signin(request):
    form = forms.SigninForm()
    return render(request,'management/signin.html', {'form' : form})


def home_admin(request):
    return render(request,'management/home-admin.html')

def home_tutor(request):
    return render(request,'management/home-tutor.html')

def home_student(request):
    return render(request,'management/home-student.html')

def home_admin(request):
    return render(request,'management/home-admin.html')
def home_admin_notice(request):
    return render(request,'management/home-admin-notice.html')
def home_admin_class(request):
    return render(request,'management/home-admin-class.html')
def home_admin_tutor(request):
    return render(request,'management/home-admin-tutor.html')
def home_admin_result(request):
    return render(request,'management/home-admin-result.html')
def home_admin_other(request):
    return render(request,'management/home-admin-other.html')

def home_tutor_notice(request):
    return render(request,'management/home-tutor-notice.html')
def home_tutor_class(request):
    return render(request,'management/home-tutor-class.html')
def home_tutor_attendance(request):
    return render(request,'management/home-tutor-attendance.html')
def home_tutor_result(request):
    return render(request,'management/home-tutor-result.html')
def home_tutor_other(request):
    return render(request,'management/home-tutor-other.html')

def home_student_notice(request):
    return render(request,'management/home-student-notice.html')

def home_student_feedback(request):
    return render(request,'management/home-student-feedback.html')
def home_student_result(request):
    return render(request,'management/home-student-result.html')
def home_student_other(request):
    return render(request,'management/home-student-other.html')

# Create your views here.

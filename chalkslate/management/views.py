from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from .models import ChalkSlateUser,notice
from .forms import ChalkSlateUserRegistrationForm, ChalkSlateAdminRegistrationForm, StudentRegistrationForm, TutorRegistrationForm, UserAuthenticationForm


from django.http import HttpResponse

# def homepage(request):
#     return render(request, 'management/homepage.html', {})

def first_func(request):
    return render(request,'management/main.html', {})

def home(request):

    context = {}

    if request.user.is_authenticated:
        chalkslate_user = ChalkSlateUser.objects.get(username = request.user.username)

        context['chalkslate_user'] = chalkslate_user

        if chalkslate_user.user_type == 3:
            related_to = chalkslate_user.student
            context['related_to'] = related_to
        elif chalkslate_user.user_type == 4:
            related_to = chalkslate_user.tutor
            context['related_to'] = related_to

    return render(request,'management/home.html', context)

def notice_board(request):

    context = {}

    if request.user.is_authenticated:
        chalkslate_user = ChalkSlateUser.objects.get(username = request.user.username)

        context['chalkslate_user'] = chalkslate_user

        if chalkslate_user.user_type == 3:
            related_to = chalkslate_user.student
            context['related_to'] = related_to
        elif chalkslate_user.user_type == 4:
            related_to = chalkslate_user.tutor
            context['related_to'] = related_to
    if request.method=='POST':

        notice.objects.create(name=request.POST.get('name'),mail=request.POST.get('mail'),date=request.POST.get('date'),content=request.POST.get('content'))

    all = notice.objects.all()
    context = {'all': all}
    return render(request,'management/notice-board.html', context)

def guide(request):
    context = {}

    if request.user.is_authenticated:
        chalkslate_user = ChalkSlateUser.objects.get(username = request.user.username)

        context['chalkslate_user'] = chalkslate_user

        if chalkslate_user.user_type == 3:
            related_to = chalkslate_user.student
            context['related_to'] = related_to
        elif chalkslate_user.user_type == 4:
            related_to = chalkslate_user.tutor
            context['related_to'] = related_to
    return render(request,'management/guide.html', context)

def about_us(request):
    context = {}

    if request.user.is_authenticated:
        chalkslate_user = ChalkSlateUser.objects.get(username = request.user.username)

        context['chalkslate_user'] = chalkslate_user

        if chalkslate_user.user_type == 3:
            related_to = chalkslate_user.student
            context['related_to'] = related_to
        elif chalkslate_user.user_type == 4:
            related_to = chalkslate_user.tutor
            context['related_to'] = related_to
    return render(request,'management/about-us.html', context)


def contact_us(request):
    context = {}

    if request.user.is_authenticated:
        chalkslate_user = ChalkSlateUser.objects.get(username = request.user.username)

        context['chalkslate_user'] = chalkslate_user

        if chalkslate_user.user_type == 3:
            related_to = chalkslate_user.student
            context['related_to'] = related_to
        elif chalkslate_user.user_type == 4:
            related_to = chalkslate_user.tutor
            context['related_to'] = related_to
    return render(request,'management/contact-us.html', context)


def register(request):
    return render(request,'management/register.html')

def reg_admin(request):

    context = {}

    if request.method == 'POST':
        chalkslate_user_registration_form = ChalkSlateUserRegistrationForm(request.POST)
        chalkslate_admin_registration_form = ChalkSlateAdminRegistrationForm(request.POST)

        if chalkslate_user_registration_form.is_valid() and chalkslate_admin_registration_form.is_valid():
            chalkslate_user = chalkslate_user_registration_form.save(commit=False)
            chalkslate_user.user_type = 2
            chalkslate_user.save()
            email = chalkslate_user_registration_form.cleaned_data.get('email')
            raw_password = chalkslate_user_registration_form.cleaned_data.get('password1')

            chalkslate_admin = chalkslate_admin_registration_form.save(commit=False)
            chalkslate_admin.chalkslate_user = chalkslate_user
            chalkslate_admin.save()

            authenticated_account = authenticate(email=email, password=raw_password)
            login(request, authenticated_account)

            return redirect('home_page')
        else:
            context['chalkslate_user_registration_form'] = chalkslate_user_registration_form
            context['chalkslate_admin_registration_form'] = chalkslate_admin_registration_form

    else: # GET request
        chalkslate_user_registration_form = ChalkSlateUserRegistrationForm()
        chalkslate_admin_registration_form = ChalkSlateAdminRegistrationForm()

        context['chalkslate_user_registration_form'] = chalkslate_user_registration_form
        context['chalkslate_admin_registration_form'] = chalkslate_admin_registration_form

    return render(request, 'management/reg-admin.html', context)





    # form = forms.AdminRegisterForm
    # return render(request,'management/reg-admin.html', {'form' : form})

def reg_tutor(request):

    context = {}

    if request.method == 'POST':
        chalkslate_user_registration_form = ChalkSlateUserRegistrationForm(request.POST)
        tutor_registration_form = TutorRegistrationForm(request.POST, request.FILES)

        if chalkslate_user_registration_form.is_valid() and tutor_registration_form.is_valid():
            chalkslate_user = chalkslate_user_registration_form.save(commit=False)
            chalkslate_user.user_type = 4
            chalkslate_user.save()
            email = chalkslate_user_registration_form.cleaned_data.get('email')
            raw_password = chalkslate_user_registration_form.cleaned_data.get('password1')

            tutor = tutor_registration_form.save(commit=False)
            tutor.chalkslate_user = chalkslate_user
            tutor.save()

            authenticated_account = authenticate(email=email, password=raw_password)
            login(request, authenticated_account)

            context['chalkslate_user'] = chalkslate_user
            context['related_to'] = tutor

            return render(request, 'management/home.html', context)
            # return redirect(reverse('home_page', context))
            # return redirect('home_page')
        else:
            context['chalkslate_user_registration_form'] = chalkslate_user_registration_form
            context['tutor_registration_form'] = tutor_registration_form

    else: # GET request
        chalkslate_user_registration_form = ChalkSlateUserRegistrationForm()
        tutor_registration_form = TutorRegistrationForm()

        context['chalkslate_user_registration_form'] = chalkslate_user_registration_form
        context['tutor_registration_form'] = tutor_registration_form

    return render(request, 'management/reg-tutor.html', context)
    # form = forms.studentRegisterForm()
    # return render(request,'management/reg-student.html', {'form' : form})

def reg_student(request):

    context = {}

    if request.method == 'POST':
        chalkslate_user_registration_form = ChalkSlateUserRegistrationForm(request.POST)
        student_registration_form = StudentRegistrationForm(request.POST, request.FILES)

        if chalkslate_user_registration_form.is_valid() and student_registration_form.is_valid():
            chalkslate_user = chalkslate_user_registration_form.save(commit=False)
            chalkslate_user.user_type = 3
            chalkslate_user.save()
            email = chalkslate_user_registration_form.cleaned_data.get('email')
            raw_password = chalkslate_user_registration_form.cleaned_data.get('password1')

            student = student_registration_form.save(commit=False)
            student.chalkslate_user = chalkslate_user
            student.save()

            authenticated_account = authenticate(email=email, password=raw_password)
            login(request, authenticated_account)

            return redirect('home_page')
        else:
            context['chalkslate_user_registration_form'] = chalkslate_user_registration_form
            context['student_registration_form'] = student_registration_form

    else: # GET request
        chalkslate_user_registration_form = ChalkSlateUserRegistrationForm()
        student_registration_form = StudentRegistrationForm()

        context['chalkslate_user_registration_form'] = chalkslate_user_registration_form
        context['student_registration_form'] = student_registration_form

    return render(request, 'management/reg-student.html', context)
    # form = forms.StudentRegisterForm()
    # return render(request,'management/reg-student.html', {'form' : form})

def signin(request):
    pass
    # form = forms.SigninForm()
    # return render(request,'management/signin.html', {'form' : form})


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

def home_student_notice(request):
    return render(request,'management/home-student-notice.html')
def home_tutor_class(request):
    return render(request,'management/home-tutor-class.html')
def home_tutor_attendance(request):
    return render(request,'management/home-tutor-attendance.html')
def home_student_result(request):
    return render(request,'management/home-student-result.html')
def home_student_other(request):
    return render(request,'management/home-student-other.html')

def home_tutor_notice(request):
    return render(request,'management/home-tutor-notice.html')

def home_student_feedback(request):
    return render(request,'management/home-student-feedback.html')
def home_tutor_result(request):
    return render(request,'management/home-tutor-result.html')
def home_tutor_other(request):
    return render(request,'management/home-student-other.html')

def logout_view(request):
    logout(request)
    return redirect('home_page')

def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home_page')

    else:
        form = UserAuthenticationForm()

    context['form'] = form

    return render(request, 'management/login_page.html', context)




# Create your views here.

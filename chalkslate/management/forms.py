from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import ChalkSlateUser, ChalkSlateAdmin, Student, Tutor

class ChalkSlateUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = ChalkSlateUser
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)

class ChalkSlateAdminRegistrationForm(forms.ModelForm):
    institute_details = forms.CharField(widget=forms.Textarea, max_length=100)

    class Meta:
        model = ChalkSlateAdmin
        fields = (
            'institute_name',
            'institute_details',
        )

class StudentRegistrationForm(forms.ModelForm):
    student_details = forms.CharField(widget=forms.Textarea, max_length=100)

    class Meta:
        model = Student
        fields = (
            'student_details',
            'picture',
        )

class TutorRegistrationForm(forms.ModelForm):
    tutor_details = forms.CharField(widget=forms.Textarea, max_length=100)

    class Meta:
        model = Tutor
        fields = (
            'tutor_details',
            'picture',
        )

class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = ChalkSlateUser
        fields = (
            'email',
        )

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid login.')

# class SigninForm(forms.Form):
#     username = forms.CharField(label='username', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : '******'}))
#
# class AdminRegisterForm(forms.Form):
#     institute_name = forms.CharField(label='Name of institute', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Name of institute'}))
#     email_address = forms.EmailField()
#     address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Name of institute'}))
#
# class TutorRegisterForm(forms.Form):
#     tutor_name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Name'}))
#     email_address = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : '******'}))
#
# class StudentRegisterForm(forms.Form):
#     student_name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Name'}))
#     email_address = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : '******'}))
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import ChalkSlateUser, ChalkSlateAdmin, Student, Tutor

# This method gets all the institutes for InstituteRegistrationForm
def get_all_institutes():
    chalkslate_admin_list = ChalkSlateAdmin.objects.all()
    return [(chalkslate_admin.institute_name, chalkslate_admin.institute_name) for chalkslate_admin in
            chalkslate_admin_list]


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

class JoinInstituteForm(forms.Form):

    institute_name = forms.ChoiceField(choices=get_all_institutes())
    note = forms.CharField(label='Note',
                           widget=forms.Textarea(attrs={
                               'placeholder' : 'Write something that will assist your institute admin to recognize you.',
                           }
                           ),
                           max_length=100)

    def __init__(self, *args, **kwargs):
        super(JoinInstituteForm, self).__init__(*args, **kwargs)
        self.fields['institute_name'] = forms.ChoiceField(choices=get_all_institutes())
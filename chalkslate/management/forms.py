from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(label='username', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : '******'}))

class AdminRegisterForm(forms.Form):
    institute_name = forms.CharField(label='Name of institute', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Name of institute'}))
    email_address = forms.EmailField()
    address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Name of institute'}))

class TutorRegisterForm(forms.Form):
    tutor_name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Name'}))
    email_address = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : '******'}))

class StudentRegisterForm(forms.Form):
    student_name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Name'}))
    email_address = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : '******'}))
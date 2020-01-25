from django import forms
from django.contrib.auth.models import User
from .models import Profile
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd  = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password don\'t match. ')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control', 'id':'firstName'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control', 'id':'lastName'})
        self.fields['email'].widget.attrs.update({'class':'form-control','id':'email'})

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({'class':'form-control', 'id':'birth', 'data-provide':'datepicker'})
        self.fields['photo'].widget.attrs.update({'class':'form-control-file', 'id':'exampleFormControlFile1' })
    
 

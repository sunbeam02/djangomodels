from django import forms
from .models import Profile

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="password", widget=forms.PasswordInput)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
        exclude =('is_verified', 'is_admin', 'is_staff', "is_seller")
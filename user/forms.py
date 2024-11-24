from django import forms
from adminpanel.models import Customer

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'country', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class LoginForm(forms.Form):
    identifier = forms.CharField(label="Email or Mobile Number")
    password = forms.CharField(widget=forms.PasswordInput)

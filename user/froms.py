from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import UserModel


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['cccd', 'email', 'is_admin', 'password1', 'password2']




from django import forms
from .models import UserModel
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    cccd = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'login-label'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'login-label'})
    )
    def clean_cccd(self):
        cccd = self.cleaned_data.get("cccd")
     

        try:
            user = UserModel.objects.get(cccd=cccd)
        except UserModel.DoesNotExist:
            raise forms.ValidationError("Tên đăng nhập hoặc mật khẩu không đúng")
        return cccd  

    def authenticate_user(self):
        cccd = self.cleaned_data.get('cccd')
        password = self.cleaned_data.get('password')
        user = authenticate(username=cccd, password=password)
        if user is None:
            raise forms.ValidationError("Tên đăng nhập hoặc mật khẩu không đúng.")
        return user

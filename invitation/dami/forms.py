from django import forms
from dami.models import User


class LoginForm(forms.Form):
    User_ID = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력해주세요', 'class': 'login-input'}),
        label='아이디',
        label_suffix='', 
    )
    Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요', 'class': 'login-input'}),
        label='비밀번호',
        label_suffix='', 
    )

class RegistrationForm(forms.Form):
    User_Name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력해주세요', 'class': 'login-input'}),
        label='이름',
        label_suffix='',
    )
    User_ID = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력해주세요', 'class': 'login-input'}),
        label='아이디',
        label_suffix='',
    )
    Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요', 'class': 'login-input'}),
        label='비밀번호',
        label_suffix='',
    )
    Password_Check = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 다시 입력해주세요', 'class': 'login-input'}),
        label='비밀번호 확인',
        label_suffix='',
    )
    User_Email = forms.EmailField(  # 'user_email'로 변경
        widget=forms.TextInput(attrs={'placeholder': '1234@.com', 'class': 'login-input'}),
        label='이메일',
        label_suffix='',
        error_messages={'invalid': '이메일 형식은 "user@example.com"과 같이 "@" 기호를 포함한 문자열이어야 합니다.'}
    )
    Phone_Number = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요', 'class': 'login-input'}),
        label='핸드폰 번호',
        label_suffix='',
    )

    # models.py
    # User_id = models.CharField(max_length=20, unique=True)
    # User_name = models.CharField(max_length=20, unique=True)
    # User_type = models.CharField(max_length=20)
    # Password_check = models.CharField(max_length=255)  # 실제로는 비밀번호를 해싱하여 저장해야 합니다.
    # Email = models.EmailField(unique=True)
    # Phone_number = models.CharField(max_length=15)

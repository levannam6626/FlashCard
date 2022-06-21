import email
from django import forms
import re
from .models import Taikhoan, Hocphan, Tudien
class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Tài khoản", max_length=20,widget=forms.TextInput(
                        attrs={'class':'username','placeholder': 'Tài khoản'}
                    ))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(
                        attrs={'class':'email','placeholder': 'Email'}
                    ))
    password = forms.CharField(label="Mật khẩu", max_length=15, widget = forms.PasswordInput(
                    attrs={'class':'password','placeholder': 'Mật khẩu'}
                    ))
    password2 = forms.CharField(label="Nhập lại Mật khẩu", max_length=15, widget = forms.PasswordInput(
                        attrs={'class':'confirmpassword','placeholder': 'Nhập lại mật khẩu'}
                    ))

    def clean_password2(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
            if password == password2 and password:
                return password2
        raise forms.ValidationError("Mật khẩu không trùng khớp")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        return username
    class Meta:
        model = Taikhoan
        fields = [
            'username',
            'email',
            'password']
class DangNhapForm(forms.ModelForm):
    username = forms.CharField(label="Tài khoản", max_length=20,
                widget=forms.TextInput(
                        attrs={'class':'username','placeholder': 'Tài khoản'}
                    ))
    password = forms.CharField(label="Mật khẩu", max_length=15, widget = forms.PasswordInput(
                        attrs={'class':'password','placeholder': 'Mật khẩu'}
                    ))

    def clean_password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            if password:
                return password
        raise forms.ValidationError("Mật khẩu không hợp lệ")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        return username
    class Meta:
        model = Taikhoan
        fields = [
            'username',
            'password']

class ThemHocPhanForm(forms.ModelForm):
    tenhocphan = forms.CharField(label="Tên học Phần", max_length=20,
                            widget=forms.TextInput(
                                                attrs={'class':'tenhocphan','placeholder': 'Tên học phần'}
                    ))
    mota = forms.CharField(label="Mô tả", max_length=200,widget=forms.TextInput(
                        attrs={'class':'mota','placeholder': 'Mô tả'}
                    ))
    taikhoan = Taikhoan
    class Meta:
        model = Hocphan
        fields = [
            'tenhocphan',
            'mota',
            'taikhoan']
class ThemTuDienForm(forms.ModelForm):
    thuatngu = forms.CharField(label="Thuật ngữ" , max_length=200,widget=forms.TextInput(
                        attrs={'class':'mota','placeholder': 'Thuật ngữ'}
                    ))
    dinhnghia = forms.CharField(label="Định Nghĩa", max_length=200,widget=forms.TextInput(
                        attrs={'class':'mota','placeholder': 'Định Nghĩa'}
                    ))
    class Meta:
        model = Tudien
        fields = [
            'thuatngu',
            'dinhnghia',
            'hocphan']
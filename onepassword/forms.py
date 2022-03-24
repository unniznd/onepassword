from django import forms


class OnePasswordForm(forms.Form):
    onepassword = forms.CharField(max_length=32, widget=forms.PasswordInput)
    keyword = forms.CharField(max_length=32, widget=forms.PasswordInput)
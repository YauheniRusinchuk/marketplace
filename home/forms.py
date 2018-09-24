from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта', required=True)
    password = forms.CharField(label='Пароль',required=True, widget=forms.PasswordInput())


    password.widget.attrs.update({'class' : 'login_password', 'placeholder' : 'ваш пароль ...'})
    email.widget.attrs.update({'class' : 'login_email', 'placeholder' : 'введите почту ...'})
    # password = forms.PasswordInput()

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms

class SignUpUserForm(UserCreationForm):
    TAILWIND_CSS_INPUTS = "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring"
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class' : TAILWIND_CSS_INPUTS, 'placeholder' : 'Ingrese su nombre de usuario'}),
        label="Nombre de usuario"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class' : TAILWIND_CSS_INPUTS, 'placeholder' : 'Ingrese su correo electrónico'}),
        label='Correo Electrónico'
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': TAILWIND_CSS_INPUTS, 'placeholder' : '••••••••'}),
        label="Contraseña"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': TAILWIND_CSS_INPUTS, 'placeholder' : '••••••••'}),
        label="Confirmar Contraseña"
    )
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

class LoginForm(AuthenticationForm):
    TAILWIND_CSS_INPUTS = "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring"
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class' : TAILWIND_CSS_INPUTS, 'placeholder' : 'Ingrese su nombre de usuario'}),
        label="Nombre de usuario"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class' : TAILWIND_CSS_INPUTS, 'placeholder' : '••••••••'}),
        label='Contraseña'
    )
    
class ChangeMetadataUserByAdminForm(forms.ModelForm):
    class Meta:
        TAILWIND_CSS_INPUTS = "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring"
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # Campos editables
        widgets = {
            'username': forms.TextInput(attrs={'class': f'{TAILWIND_CSS_INPUTS}'}),
            'email': forms.EmailInput(attrs={'class': f'{TAILWIND_CSS_INPUTS}'}),
            'first_name': forms.TextInput(attrs={'class': f'{TAILWIND_CSS_INPUTS}'}),
            'last_name': forms.TextInput(attrs={'class': f'{TAILWIND_CSS_INPUTS}'}),
        }

class ChangePasswordUserByAdminForm(SetPasswordForm):
    TAILWIND_CSS_INPUTS = "block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring"
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # El usuario cuya contraseña se cambiará
        super().__init__(self.user, *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': f'{self.TAILWIND_CSS_INPUTS}',
                'placeholder': f'Ingrese {field.label.lower()}'
            })
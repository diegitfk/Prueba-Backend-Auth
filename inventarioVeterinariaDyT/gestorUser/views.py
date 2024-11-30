from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpRequest , HttpResponse
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import View, ListView
from . import forms

# Create your views here.

class CreateUserView(View):
    def get(self , request : HttpRequest) -> HttpResponse:
        form_create_user = forms.SignUpUserForm()
        return render(request , 'authentication/signup.html' , {'form' : form_create_user})
    
    def post(self , request : HttpRequest) -> HttpResponse:
        form_create_user = forms.SignUpUserForm(request.POST)
        if form_create_user.is_valid():
            form_create_user.save()
            form_create_user = forms.SignUpUserForm()
            return render(request , 'authentication/signup.html' , {'form' : form_create_user , 'sign_up_state' : True})
        else:
            return render(request , 'authentication/signup.html' , {'form' : form_create_user , 'sign_up_state' : False})

class LoginCustomView(LoginView):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'
    
    def form_valid(self, form):
        # Lógica cuando el formulario es válido (login exitoso)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Esto se ejecuta cuando el formulario es inválido, lo que pasa cuando hay errores de validación
        return self.render_to_response(self.get_context_data(form=form))

class UsersView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest) -> HttpResponse:
        user_list = User.objects.filter(is_superuser=False).all()
        user_list = list(user_list)
        return render(request , 'dashboard/usuarios/admin_usuarios.html' , {'users' : user_list})
    
class UsersUpdatePasswordView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest , id_user : int) -> HttpResponse:
        user = User.objects.filter(id=id_user).first()
        form_change_password = forms.ChangePasswordUserByAdminForm(user=user)
        return render(request , 'dashboard/usuarios/editar_password_usuario.html' , context={'form' : form_change_password , 'user_change' : user})
        
    def post(self , request : HttpRequest , id_user : int) -> HttpResponse:
        user = User.objects.filter(id=id_user).first()
        form_change_password = forms.ChangePasswordUserByAdminForm(user=user , data=request.POST)
        if form_change_password.is_valid():
            form_change_password.save()
            return redirect(reverse('admin-usuarios'))
        else:
            return render(request , 'dashboard/usuarios/editar_password_usuario.html' , context={'form' : form_change_password , 'user_change' : user})

class UsersUpdateMetadataView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest , id_user : int) -> HttpResponse:
        user = User.objects.get(id=id_user)
        form_change_metadata = forms.ChangeMetadataUserByAdminForm(instance=user)
        return render(request , 'dashboard/usuarios/editar_datos_usuario.html' , context={'form' : form_change_metadata , 'user_change' : user})
    
    def post(self , request : HttpRequest , id_user : int) -> HttpResponse:
        user = User.objects.filter(id=id_user).first()
        form_change_metadata = forms.ChangeMetadataUserByAdminForm(request.POST , instance=user)
        if form_change_metadata.is_valid():
            form_change_metadata.save()
            return redirect(reverse('admin-usuarios'))
        else:
            return render(request , 'dashboard/usuarios/editar_datos_usuario.html' , context={'form' : form_change_metadata , 'user_change' : user})

class UsersDeleteView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest , id_user : int) -> HttpResponse:
        user_del = User.objects.get(id=id_user)
        user_del.delete()
        users = User.objects.filter(is_superuser=False).all()
        users = list(users)
        return render(request , 'dashboard/usuarios/admin_usuarios.html' , {'users' : users})

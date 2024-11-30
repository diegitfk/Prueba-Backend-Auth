from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views
#Aqui se manejan las URL proporcionadas por Django para la autenticación.
urlpatterns = [
    path('login/' , views.LoginCustomView.as_view() , name='login'),
    path('logout/' , auth_views.LogoutView.as_view() , name='logout'),
    path('signup/' , views.CreateUserView.as_view() , name="signup"),
    path('see_users/' , views.UsersView.as_view() , name='admin-usuarios'),
    path('update_password_user/<int:id_user>' , view=views.UsersUpdatePasswordView.as_view() ,name="actualizar-contraseña-usuarios"),
    path('update_metadata_user/<int:id_user>' , view=views.UsersUpdateMetadataView.as_view() , name='actualizar-datos-usuarios'),
    path('delete_user/<int:id_user>/' ,view= views.UsersDeleteView.as_view() ,name="eliminar-usuarios" ),
]
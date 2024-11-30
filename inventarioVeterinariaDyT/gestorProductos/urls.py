from django.urls import path , include
from . import views
urlpatterns = [
    path('' , views.DashView.as_view(), name="dash-index"),
    path('see_products/' , views.ProductsView.as_view() , name='ver-productos'),
    path('create_product/' , view=views.CreateProductsView.as_view() , name='crear-productos'),
    path('update_product/<int:id_product>/' , view=views.UpdateProductsView.as_view() ,  name="actualizar-productos"),
    path('delete_product/<int:id_product>/' , view=views.DeleteProductsView.as_view() , name="eliminar-productos"),
    path('see_categories/' , views.CategoriaView.as_view() , name="admin-categorias"),
    path('create_categorie/' , view=views.CreateCategoriaView.as_view() , name="crear-categorias"),
    path('update_categorie/<int:id_categorie>/' , view=views.UpdateCategoriaView.as_view() , name="actualizar-categorias"),
    path('delete_categorie/<int:id_categorie>/' , view=views.DeleteCategoriaView.as_view() , name='eliminar-categorias')
]
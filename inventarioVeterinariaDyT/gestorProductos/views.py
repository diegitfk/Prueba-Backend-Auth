from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpRequest , HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
# Create your views here.
class DashView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest) -> HttpResponse:
        return render(request , 'dashboard/index_dashboard.html')

class ProductsView(LoginRequiredMixin , View):
    
    def get(self , request : HttpRequest) -> HttpResponse:
        if request.user.is_superuser:
            products = models.Producto.objects.all()
            product_list = list(products)
            return render(request , 'dashboard/productos/ver_productos.html' , {'products' : product_list})
        else:
            products = models.Producto.objects.filter(creado_por=request.user.id)
            product_list = list(products)
            return render(request , 'dashboard/productos/ver_productos.html' , {'products' : product_list})

class CreateProductsView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest) -> HttpResponse:
        form = forms.ProductGeneralForm()
        return render(request , 'dashboard/productos/crear_producto.html' , {'form' : form})
    
    def post(self , request : HttpRequest) -> HttpResponse:
        form = forms.ProductGeneralForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creado_por = request.user
            instance.save()
            return redirect(reverse('ver-productos'))
        else:
            return render(request , 'dashboard/productos/crear_producto.html' , {'form' : form})
        

class UpdateProductsView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest , id_product : int) -> HttpResponse:
        product = models.Producto.objects.get(id=id_product)
        form_update = forms.ProductGeneralForm(instance=product)
        return render(request , 'dashboard/productos/actualizar_producto.html' , {'form' : form_update , 'product' : product})
    
    def post(self , request : HttpRequest , id_product : int) -> HttpResponse:
        product = models.Producto.objects.get(id=id_product)
        form_update = forms.ProductGeneralForm(request.POST , instance=product)
        if form_update.is_valid():
            instance = form_update.save(commit=False)
            instance.creado_por = request.user
            instance.save()
            return redirect(reverse('ver-productos'))
        else:
            product = models.Producto.objects.get(id=id_product)
            return render(request , 'dashboard/productos/actualizar_producto.html' , {'form' : form_update , 'product' : product})


class DeleteProductsView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest , id_product : int) -> HttpResponse:
        product_del = models.Producto.objects.get(id=id_product)
        product_del.delete()
        products = models.Producto.objects.all()
        product_list = list(products)
        return render(request , 'dashboard/productos/ver_productos.html' , {'products' : product_list})

class CategoriaView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest) -> HttpResponse:
        categories = models.Categoria.objects.all()
        cat_list = list(categories)
        return render(request , 'dashboard/categorias/admin_categorias.html' , {'categories' : cat_list})

class CreateCategoriaView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest) -> HttpResponse:
        form = forms.CategorieGeneralForm()
        return render(request , 'dashboard/categorias/crear_categoria.html' , {'form' : form})
    
    def post(self , request : HttpRequest) -> HttpResponse:
        form = forms.CategorieGeneralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-categorias'))
        else:
            return render(request , 'dashboard/categorias/crear_categorias.html' , {'form' : form})

class UpdateCategoriaView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest , id_categorie : int) -> HttpResponse:
        cat = models.Categoria.objects.get(id=id_categorie)
        form_update = forms.CategorieGeneralForm(instance=cat)
        return render(request , 'dashboard/categorias/actualizar_categoria.html' , {'form' : form_update , 'cat' : cat})
    
    def post(self , request : HttpRequest , id_categorie : int) -> HttpResponse:
        cat = models.Categoria.objects.get(id=id_categorie)
        form_update = forms.CategorieGeneralForm(request.POST , instance=cat)
        if form_update.is_valid():
            form_update.save()
            return redirect(reverse('admin-categorias'))
        else:
            cat = models.Categoria.objects.get(id=id_categorie)
            return render(request , 'dashboard/categorias/actualizar_categoria.html' , {'form' : form_update , 'cat' : cat})

class DeleteCategoriaView(LoginRequiredMixin , View):
    def get(self , request : HttpRequest , id_categorie : int) -> HttpResponse:
        cat_del = models.Categoria.objects.get(id=id_categorie)
        cat_del.delete()
        categories = models.Categoria.objects.all()
        categories = list(categories)
        return render(request , 'dashboard/categorias/admin_categorias.html' , {'categories' : categories})
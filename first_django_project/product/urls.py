from django.contrib import admin
from django.urls import path
from .views import product_view,ProductDetailView,field_lookup,category_deatail_view

urlpatterns = [
    path('products/',product_view.as_view()),
    path('products/<int:pk>',ProductDetailView.as_view(),name="productdetail"),#in detailView we only join primary key
    path('productlookup/',field_lookup),
    path('category/<slug:slug>',category_deatail_view.as_view(),name="category")

]
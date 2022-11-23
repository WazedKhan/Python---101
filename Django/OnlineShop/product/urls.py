from django.urls import path

from product.views import index, create_category

urlpatterns = [
    path('category-list', index, name='category-list'),
    path('category-create', create_category, name='category-create'),
] 
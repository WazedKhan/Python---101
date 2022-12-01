from django.urls import path

from product.views import index, create_category, update_category

urlpatterns = [
    path('category-list/', index, name='category-list'),
    path('category-create/', create_category, name='category-create'),
    path('category/<int:id>/update/', update_category, name='category-update'),
]

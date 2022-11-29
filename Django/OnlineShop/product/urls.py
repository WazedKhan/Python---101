from django.urls import path

from product.views import index, create_category, category_update

urlpatterns = [
    path('category-list/', index, name='category-list'),
    path('category-create/', create_category, name='category-create'),
    path('category/<int:id>', category_update, name='category-update'),
]

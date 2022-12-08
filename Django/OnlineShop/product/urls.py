from django.urls import path

from product.views import (
    index, create_category, category_update, 
    category_delete, ProductListView, ProductDetailView
)

urlpatterns = [
    path('category-list/', index, name='category-list'),
    path('category-create/', create_category, name='category-create'),
    path('category/<int:id>', category_update, name='category-update'),
    path('category/<int:id>/delete', category_delete, name='category-delete'),

    path('', ProductListView.as_view(), name='product-list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product-detail')
]

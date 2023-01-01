from django.urls import path

from product.views import (
    index, create_category, category_update, add_cart, cart_list,
    category_delete, ProductListView, ProductDetailView,ProductCreateView
)

urlpatterns = [
    path('category-list/', index, name='category-list'),
    path('category-create/', create_category, name='category-create'),
    path('category/<int:id>', category_update, name='category-update'),
    path('category/<int:id>/delete', category_delete, name='category-delete'),

    path('', ProductListView.as_view(), name='product-list'),
    path('create', ProductCreateView.as_view(), name='product-create'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('add/cart', add_cart, name='add-cart'),
    path('cart/list', cart_list, name='cart-list'),
]

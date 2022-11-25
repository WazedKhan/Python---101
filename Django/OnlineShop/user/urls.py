from django.urls import path
from user import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('registration/', views.registration, name='registration')
]

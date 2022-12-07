from django.urls import path
from user import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('login-view', views.login_view, name='login-view'),
    path('logout-view', views.logout_view, name='logout-view'),
    path('registration/', views.registration, name='registration')
]

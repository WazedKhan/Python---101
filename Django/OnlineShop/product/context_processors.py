from django.contrib.sessions.models import Session
from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}
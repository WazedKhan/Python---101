from django.shortcuts import render
from product.models import Category

# Create your views here.

def index(request):
    category = Category.objects.all()
    context = {'data': category}
    return render(request, 'index.html', context)

def create_category(request):
    return render(request, 'category-create.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse

from product.models import Category

# Create your views here.

def index(request):
    category = Category.objects.all()
    context = {'data': category}
    return render(request, 'index.html', context)

def create_category(request):
    if request.method == "POST":
        Category.objects.create(
            name=request.POST.get('category'),
            user=request.user
        )
        return redirect('category-list')

    return render(request, 'category-create.html')

def update_category(request, id):
    data = Category.objects.get(id=id)
    if request.method == 'POST':
        data.name = request.POST.get('category')
        data.save()
        return redirect('category-list')
    return render(request, 'category-update.html', {'name': data})

# data.delete
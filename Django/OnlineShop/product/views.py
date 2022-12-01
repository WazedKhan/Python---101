from django.shortcuts import render
from django.shortcuts import redirect

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


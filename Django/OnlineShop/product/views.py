from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from product.models import Category, Product

# Create your views here.

def index(request):
    category = Category.objects.all()
    context = {'data': category}
    return render(request, 'index.html', context)

@login_required
def create_category(request):
    if request.method == "POST":
        Category.objects.create(
            name=request.POST.get('category'),
            user=request.user
        )
        return redirect('category-list')

    return render(request, 'category-create.html')


def category_update(request, id):
    data = Category.objects.get(id = id)
    if request.method == 'POST':
        data.name = request.POST.get('category')
        data.save()
        return redirect('category-list')
    return render(request, 'category-update.html', {'val': data})

def category_delete(request, id):
    category = Category.objects.get(id = id)
    category.delete()
    return redirect('category-list')

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product-list.html'

    # def get_queryset(self):
    #     return self.model.objects.filter(in_stock=True)

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product-detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'price', 'category']
    template_name = 'product-create.html'
    success_url = reverse_lazy('product-list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'price', 'category']
    template_name = 'product-update.html'
    success_url = reverse_lazy('product-list')
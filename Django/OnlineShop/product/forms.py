from django import forms
from django.contrib.auth.models import User

from product.models import Category

class CategoryUpdateForm(forms.ModelForm):


    class Meta:
        model = Category
        fields = ['name']
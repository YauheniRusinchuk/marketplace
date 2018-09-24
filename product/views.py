from django.shortcuts import render, redirect
from product.forms import ProductForms
from product.models import ImageProduct, Products
from django.forms import modelformset_factory
from datetime import date, timedelta, datetime
# Create your views here.

def add_product(request):
    form = ProductForms()
    imgform = modelformset_factory(ImageProduct, fields=('othersphoto',), extra=5)
    formset = imgform(queryset=ImageProduct.objects.none())
    if request.method == 'POST':
        postform = ProductForms(request.POST or None, request.FILES or None)
        if postform.is_valid():
            now = datetime.now()
            delete = now + timedelta(days=10)
            img = request.FILES.get('photo')
            product = Products(title=request.POST['title'].upper(),
                        description=request.POST['description'],
                        city=request.POST['city'].capitalize(),
                        price=request.POST['price'],
                        photo=img, delete=delete
            )
            product.save()
            return redirect('home:index_page')
    return render(request, 'product/add_product.html', {'form': form, 'formset': formset})

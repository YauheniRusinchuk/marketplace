from django.shortcuts import render
from product.models import Products
from datetime import date, timedelta, datetime
from django.views.generic import DetailView


# Create your views here.
def index(request):
    products = Products.objects.all()
    today = date.today()
    # print(today)
    time = today + timedelta(days=5)
    # print(time)
    now = datetime.now()
    # print(now.date())
    return render(request, 'home/index.html', {'products': products})


class DetailPost(DetailView):
    context_object_name = 'post'
    model = Products
    template_name = 'home/detail.html'

from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home_Page(request):
    return render(request, 'Courier/home.html')

def dashboard_Page(request):
    return render(request, 'Courier/dashboard.html')


def customer_Page(request):
    return render(request, 'Courier/customer.html')

def products_Page(request):
    return render(request, 'Courier/products.html')        
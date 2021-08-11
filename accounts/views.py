from django.shortcuts import render
from django.http import HttpResponse
def Home(request):
    return render(request, 'accounts/dashboard.html')


def Product(request):
    return render(request, 'accounts/products.html')

def Customer(request):
    return render(request, 'accounts/customer.html')



# Create your views here.

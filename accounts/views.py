from django.shortcuts import render
from django.http import HttpResponse
def Home(request):
    return render(request, 'accounts/dashboard.html')


def Product(request):
    return HttpResponse('Product')

def Customer(request):
    return HttpResponse('Customer')



# Create your views here.

from django.urls import  path
from .import views


urlpatterns = [
    path('Home', views.Home),
    path('Product', views.Product),
    path('Customer', views.Customer)

]

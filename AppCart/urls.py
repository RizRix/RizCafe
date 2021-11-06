from django.urls import path
from . import views

urlpatterns = [

    path('cart_details', views.cart_details, name='cart_details'),
    path('add/<int:id>/', views.add_cart, name='add'),
    path('min/<int:id>/', views.min_cart, name='min'),
    path('del/<int:id>/', views.delete, name='del')
]

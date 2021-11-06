from django.urls import path
from . import views

urlpatterns=[
    path('<slug:cslug>/<slug:pslug>', views.Display, name='Display'),
    path('<slug:cslug>/', views.pro_menu, name='pro_menu'),

    path('update/', views.update, name='update'),
    path('menu', views.pro_menu, name='menu'),

    path('search',views.search,name='search'),
    path('searching', views.searching, name='searching'),

    path('',views.home,name='home')




]
from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def home(request):
    cat = Category.objects.all()

    return render(request, 'index.html', {'cat': cat})


def update(request):
    return render(request, 'settings.html')


def search(request):
    return render(request, 'search.html')


def pro_menu(request, cslug=None):
    c_page = None
    pro = None
    if cslug is not None:
        c_page = get_object_or_404(Category, cslug=cslug)
        pro = Products.objects.filter(pcategory=c_page, pavailable=True)
    else:
        pro = Products.objects.all().filter(pavailable=True)

    cat = Category.objects.all()

    paginator = Paginator(pro, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pg = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pg = paginator.page(paginator)

    return render(request, 'menu.html', {'pr': pro, 'ct': cat, 'pg': pg})


def Display(request, cslug, pslug):
    try:
        prod = Products.objects.filter(pcategory__cslug=cslug, pslug=pslug)
    except Exception as e:
        raise e

    return render(request, 'details.html', {'pr': prod})


def detail(request, pid):
    pd = Products.objects.filter(id=pid)
    return render(request, 'details.html', {'pd': pd})


def searching(request):
    prod = None
    qy = None
    if 'q' in request.GET:
        qy = request.GET.get('q')
        prod = Products.objects.all().filter(Q(pname__icontains=qy) | Q(pdes__icontains=qy))

    return render(request, 'search.html', {'qr': qy, 'pr': prod})

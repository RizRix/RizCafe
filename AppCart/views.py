from django.shortcuts import render, redirect, get_object_or_404
from CafeApp.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required



@login_required()
def add_cart(request, id):

    prod = Products.objects.get(id=id)
    owner = request.user
    try:
        ct = CartList.objects.get(user=owner)
    except CartList.DoesNotExist:
        ct = CartList.objects.create(user=owner)
        ct.save()
    try:
        c_items = Items.objects.get(prodt=prod, cart=ct)
        if c_items.iquan < c_items.prodt.pstock:
            c_items.iquan += 1
        c_items.save()
    except Items.DoesNotExist:
        c_items = Items.objects.create(prodt=prod, iquan=1, cart=ct)
        c_items.save()

    return redirect('cart_details')

@login_required()
def cart_details(request, tot=0, count=0, cart_items=None):
    owner=request.user
    try:
        ct = CartList.objects.get(user=owner)
        ct_items = Items.objects.filter(cart=ct, iactive=True)
        for i in ct_items:
            tot += (i.prodt.pprice * i.iquan)
            count += i.iquan
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})


def min_cart(request, id):
    owner=request.user
    ct = CartList.objects.get(user=owner)
    prod = get_object_or_404(Products, id=id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    if c_items.iquan > 1:
        c_items.iquan -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart_details')


def delete(request, id):
    owner = request.user
    ct = CartList.objects.get(user=owner)
    prod = get_object_or_404(Products, id=id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cart_details')

from django.db import models
from CafeApp.models import *
from django.contrib.auth.models import User


# Create your models here.
class CartList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sid


class Items(models.Model):
    prodt = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList, on_delete=models.CASCADE)
    iquan = models.IntegerField()
    iactive = models.BooleanField(default=True)

    def __str__(self):
        return self.pid

    def total(self):
        return self.prodt.pprice*self.iquan

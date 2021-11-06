from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'cslug': ['cname', ]}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'pslug': ['pname', ]}
    list_display = ['pname','pcategory','pprice','pstock','pavailable']
    list_editable = ['pcategory','pprice','pstock','pavailable']


admin.site.register(Products, ProductAdmin)

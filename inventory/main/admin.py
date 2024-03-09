from django.contrib import admin
from .import models

# Register your models here.

class CoustomerAdmin(admin.ModelAdmin):
    search_fields = ['customer_name', 'customer_mobile','customer_address']
    list_display = ['customer_name','customer_mobile','customer_address']
admin.site.register(models.Coustomer,CoustomerAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display = ['full_name','address','mobile','status']
admin.site.register(models.Vendor,VendorAdmin)


class UnitAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(models.Unit,UnitAdmin)

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'unit__title']
    list_display = ['title','detail','unit',]
admin.site.register(models.Product,ProductAdmin)

class PurchaceAdmin(admin.ModelAdmin):
    search_fields = ['product__title']
    list_display = ['id','vendor','product','quality','price','total_amount','vendor', 'purchace_date']
admin.site.register(models.Purchace,PurchaceAdmin)


class SellAdmin(admin.ModelAdmin):
    search_fields = ['product__title']
    list_display = ['id','coustomer','product','quality','price','coustomer','total_amount','sell_date']
admin.site.register(models.Sell,SellAdmin)


class InventoryAdmin(admin.ModelAdmin):
    search_fields = ['product__title','product__unit__title']
    list_display = ['product','puechace_quality','sell_quality','total_balance_quality','product_unit','purchace_date', 'sell_date']

admin.site.register(models.Inventory,InventoryAdmin)

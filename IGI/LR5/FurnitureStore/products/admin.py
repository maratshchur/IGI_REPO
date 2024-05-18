from django.contrib import admin
from .models import PickupPoint, Product, ProductType, Promocode, Order

admin.site.register(PickupPoint)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Promocode)
admin.site.register(Order)

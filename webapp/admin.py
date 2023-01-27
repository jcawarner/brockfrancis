from django.contrib import admin
from .models import Drill, Component, Center, CenterQuantity


admin.site.register(Drill)
admin.site.register(Component)
admin.site.register(Center)
admin.site.register(CenterQuantity)

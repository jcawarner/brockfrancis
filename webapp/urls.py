from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drill_info/', views.drill_info, name='drill_info'),
    path('drill_info/save/', views.save, name='save'),
    path('drill_info/inventory/', views.inventory, name='inventory'),
    path('drill_info/center_created/<str:center>', views.center_created, name='center_created'),
    path('drill_info/center_saved/<str:center>', views.center_saved, name='center_saved'),
]
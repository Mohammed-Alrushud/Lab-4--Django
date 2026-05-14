from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:number>', views.calculate),
    path('taxrate', views.taxrate),
]
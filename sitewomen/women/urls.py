from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index, name='home'),
    path('after.html/', views.after, name='after'),
    path('material.html/', views.material, name='material'),
    path('mn.html/', views.mn, name='mn'),
    path('olympics.html/', views.olympics, name='olympics')
]


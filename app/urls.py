from django.urls import path
from app.views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('all-location',Location.as_view(),name='all-location'),
    path('all-productmovement',Movements.as_view(),name='all-productmovement'),
    path('add-product',AddProduct.as_view(),name='add-product'),
    path('add-location',AddLocation.as_view(),name='add-location'),
    path('add-productmovement',AddProductMovement.as_view(),name='add-productmovement'),
    path('update-product/<int:pk>',UpdateProduct.as_view(),name='update-product'),
    path('update-location/<int:pk>',UpdateLocations.as_view(),name='update-location'),
    path('update-product-movement/<int:pk>',UpdateMovement.as_view(),name='update-product-movement'),
    path('report',Report.as_view(),name='report')
]
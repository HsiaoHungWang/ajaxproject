from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.index),
    # http://127.0.0.1:8000/json
    path('json/', views.json_demo),    
    # http://127.0.0.1:8000/first
    path('first/', views.first),
    # http://127.0.0.1:8000/address
    path('address/', views.address),
    # http://127.0.0.1:8000/image
    path('image/', views.show_image)
    ]
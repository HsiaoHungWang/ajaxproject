from django.urls import path
from . import views
urlpatterns = [
    # http://127.0.0.1:8000/api
    path('', views.index),
    # http://127.0.0.1:8000/api/cities
    path('cities/', views.cities),
    # # http://127.0.0.1:8000/api/districts?city=金門縣
    # path('districts/', views.districts),
    # http://127.0.0.1:8000/api/districts/金門縣
    path('districts/<str:city_name>', views.districts),
    # http://127.0.0.1:8000/api/roads/新北市板橋區
    path('roads/<str:district>', views.roads),
    # http://127.0.0.1:8000/api/show
    path('show/', views.show),
      # http://127.0.0.1:8000/api/register
    path('register/', views.register)
]
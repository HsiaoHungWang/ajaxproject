from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Address
# Create your views here.
def index(reqeust):
    content='Hello Ajax!!'
    # response = HttpResponse(content, 'text/plain')
    # 回傳文字內容
    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    return response

def cities(request):
    cities = Address.objects.values('city').distinct()
    print(cities)
    cities = [item['city'] for item in cities]
    # item => {'city': '新竹縣'}
    # print(cities)
    return JsonResponse(cities, safe=False)

# /api/districts/金門縣
# /api/districts/?city_name=金門縣
def districts(request, city_name):
    districts = Address.objects.filter(city=city_name).values('site_id').distinct()
    print(districts)
    districts = [item['site_id'] for item in districts]
    return JsonResponse(districts, safe=False)

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
    cities = [item['city'] for item in cities]
    # print(cities)
    return JsonResponse(cities, safe=False)


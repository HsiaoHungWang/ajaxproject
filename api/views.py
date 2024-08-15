from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
import time
from .models import Address, Member
# Create your views here.
def index(reqeust):
    time.sleep(5)
    content='Hello Fetch!!'
    # response = HttpResponse(content, 'text/plain')
    # 回傳文字內容
    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    return response

def cities(request):
    cities = Address.objects.values('city').distinct()
    # print(cities)
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

def roads(request, site_id):
    pass

# /api/show?id=3
def show(request):
#    取得 ?id=3 的資料
   id = request.GET.get('id', 1)
#   根據 id 讀取 會員資料
   member = Member.objects.get(user_id=id)
   file_name = member.user_avator
   img = open('uploads/' + file_name, 'rb')
#    img = open('static/images/loading.gif', 'rb')
   return FileResponse(img)

# /api/register/?name=Tom&email=Tom@company.com&age=30
def register(request):
#    取得 ?id=3 的資料
   name = request.GET.get('name', 'Guest')
   email = request.GET.get('email', 'Guest@company.com')
   age = request.GET.get('age', 30)

   content = f"{name} 您好，電子郵件是 {email}，{age} 歲了."

   return HttpResponse(content, 'text/plain')

def check_name(request):
    # filter(name='Tom').exists()
    pass

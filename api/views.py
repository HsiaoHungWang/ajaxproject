from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
import time
import json
from .models import Address, Member
from django.core.files.storage import FileSystemStorage

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

# 傳資料進districts function GET 有兩種做法
# 1. GET /api/districts/金門縣  => urls.py 路由參數 path('districts/<str:city_name>', views.districts),
# 2. GET /api/districts/?city_name=金門縣&key=value
def districts(request, city_name):  # 1
    # 接收資料也有兩種做法
    # 2 request.GET.get('key')
    districts = Address.objects.filter(city=city_name).values('site_id').distinct()
    # print(districts)
    districts = [item['site_id'] for item in districts]
    return JsonResponse(districts, safe=False)

# 根據鄉鎮區的名稱帶出路名
def roads(request, district):
    # 根據 district 篩選路名
    roads = Address.objects.filter(site_id = district).values('road')
    roads = [item['road']  for item in roads]

    return JsonResponse(list(roads), safe=False)

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
#    接收GET傳過來的資料
#    取得 ?id=3 的資料
#    name = request.GET.get('name', 'Guest')
#    email = request.GET.get('email', 'Guest@company.com')
#    age = request.GET.get('age', 30)
# 接收POST傳過來FormData的資料
   name = request.POST.get('name', 'Guest')
   email = request.POST.get('email', 'Guest@company.com')
   age = request.POST.get('age', 30)

#  接收傳過來的檔案
   uploaded_file = request.FILES.get('avatar')
#    把檔案寫進uploads資料夾
   if uploaded_file:
       fs = FileSystemStorage()
       file_name = fs.save(uploaded_file.name, uploaded_file)

   content = f"{name} 您好，電子郵件是 {email}，{age} 歲了. {file_name}"

   return HttpResponse(content, 'text/plain')

def check_name(request):
    # filter(name='Tom').exists()
    pass

def register1(request):
    user = json.loads(request.body) # 將JSON字串反序列化成dict物件
    name = user.get('name')
    email = user.get('email')
    age = user.get('age')
    content = f"{name} 您好，電子郵件是 {email}，{age} 歲了. "
    return HttpResponse(content, 'text/plain')

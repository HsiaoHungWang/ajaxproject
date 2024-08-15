from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html',{'title':'async await'})
def json_demo(request):
    return render(request, 'home/json.html',{'title':'JSON 練習'})
def first(request):
    return render(request, 'home/first.html',{'title':'使用 fetch()'})
def address(request):
    return render(request, 'home/address.html',{'title':'取得JSON資料'})
def show_image(request):
    return render(request, 'home/show_image.html',{'title':'取得檔案(圖)'})
def register(request):
    return render(request, 'home/register.html',{'title':'會員註冊'})

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html',{'title':'async await'})
def json_demo(request):
    return render(request, 'home/json.html',{'title':'JSON 練習'})

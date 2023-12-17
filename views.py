from django.shortcuts import render
from django.http import HttpResponse
from applii.forms import customersForm

# Create your views here.
def jan(request):
    return render(request,'jan.html')


def gm_veiw(request):
    return HttpResponse('<h1> Good morning </h1>')
def ge_view(request):
    return HttpResponse('<h1>Good evening</h1>')
def gn_view(request):
    return HttpResponse('<h1>Good night</h1>')

def hello(request):
    return render(request,'hello.html')


def custom(request):
    stu=customersForm()
    return render(request,"student.html",{'form':stu})
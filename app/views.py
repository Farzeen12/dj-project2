from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pasapugal(request):
    return HttpResponse('<h1><marquee>pasapugal is a genius</h1>')

def tonystark(request):
    return HttpResponse('''<h1>I AM RICH</h1>
    <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPu4yv470qk3k26wSYTxGDJb8viXoOhykCCg&s'>''')

def me(request):
    return HttpResponse(''' <h1>I HAVE A BMW M5 CS</h1>
    <img src ='https://mediapool.bmwgroup.com/cache/P9/202104/P90418386/P90418386-portimo-por-15th-april-2021-bmw-m-gmbh-2021-bmw-m-award-motogp-winner-s-car-bmw-m5-cs-600px.jpg'>''')
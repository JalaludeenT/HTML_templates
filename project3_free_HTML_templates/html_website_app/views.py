from django.shortcuts import render, redirect
from .models import News


# Create your views here.


def home(request):
    obj = News.objects.all()
    return render(request, 'index.html', {'result': obj})

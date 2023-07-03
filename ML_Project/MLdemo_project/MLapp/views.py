from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Programming,Course
from django.core import serializers
import json


# Create your views here.
def demo(request):
    return render(request,'index.html')
def index(request):
    program=Programming.objects.all()
    d={'program':program}
    return render(request,"home.html",d)
def load_courses(request):
    programming_id=request.GET.get('programming')
    courses=Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request,"form.html",{'courses':courses})
def submit(request):
    return render(request, 'order_success.html')

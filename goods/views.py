from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json





def goods(request):
    f=open("data.json",encoding='UTF-8')
    data=json.load(f)
    res={}
    res['errno']=0
    res['data']=data['goods']
    return HttpResponse(json.dumps(res),content_type="application/json")


def ratings(request):
    f=open("data.json",encoding='UTF-8')
    data=json.load(f)
    res={}
    res['errno']=0
    res['data']=data['ratings']
    return HttpResponse(json.dumps(res),content_type="application/json")

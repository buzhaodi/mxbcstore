from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from .models import goods,types




def good(request):
    f=open("data.json",encoding='UTF-8')

    data=json.load(f)['goods']
    data = list(types.objects.all().values())
    for type in data:
        foods=list(goods.objects.filter(type_id=type['id']).values())
        type['foods']=foods



    res={}

    res['errno']=0
    res['data']=data
    return HttpResponse(json.dumps(res),content_type="application/json")


def ratings(request):
    f=open("data.json",encoding='UTF-8')
    data=json.load(f)
    res={}
    res['errno']=0
    res['data']=data['ratings']
    return HttpResponse(json.dumps(res),content_type="application/json")

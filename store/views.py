from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import Store,infos , pics ,supports
# Create your views here.

def seller(request):
    storenum=request.GET['id']
    f=open("data.json",encoding='UTF-8')
    data=json.load(f)
    res={}
    res['errno']=0
    res['data'] = data['seller']
    data=list(Store.objects.filter(num=storenum).values())[0]
    picslist= list(pics.objects.filter(store_id=data['id']).values('info'))
    endpiclist=[]
    for pic in picslist:
        endpiclist.append(pic['info'])
    data['pics']=endpiclist

    infoslist=list(infos.objects.filter(store_id=data['id']).values('info'))
    endinfos=[]
    for info in infoslist:
        endinfos.append(info['info'])
    data['infos']=endinfos

    supportslist=list(supports.objects.filter(store_id=data['id']).values())
    endsupports=[]
    # for support in supportslist:
    #     endinfos.append(support['support'])
    data['supports']=supportslist



    res['data'] = data
    return HttpResponse(json.dumps(res),content_type="application/json")

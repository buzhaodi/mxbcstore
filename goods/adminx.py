from .models import *
import xadmin
# Register your models here.

# class MyAdminSite(xadmin.AdminSite):
#     site_header = '蜜雪冰城装修记录'  # 此处设置页面显示标题
#     site_title = '蜜雪冰城装修情况'  # 此处设置页面头部标题
#
#
# xadmin.sites = MyAdminSite(name='management')

class goodsadmin(object):
    list_display = ['icon','type','name','price','oldprice','sellCount']
    list_filter = ['type','name','price','oldprice']
    search_fields = ['type','price','oldprice']
    style_fields = {'stores': 'm2m_transfer'}
    model_icon = 'fa fa-asterisk'



class ratingsadmin(object):
    list_display = ['avatar','user','time','rateType','text']
    list_filter = ['user','rateType','time']
    search_fields = ['user','rateType','text','time']
    model_icon = 'fa fa-list'






xadmin.site.register(goods,goodsadmin)

xadmin.site.register(types)

xadmin.site.register(ratings,ratingsadmin)



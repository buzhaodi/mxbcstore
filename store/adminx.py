from .models import *
import xadmin
# Register your models here.

# class MyAdminSite(xadmin.AdminSite):
#     site_header = '蜜雪冰城装修记录'  # 此处设置页面显示标题
#     site_title = '蜜雪冰城装修情况'  # 此处设置页面头部标题
#
#
# xadmin.sites = MyAdminSite(name='management')





class companyAdmin(object):
    list_display = ['pk','cname','ctel','cworker']
    list_filter = ['cname']
    search_fields = ['cname','ctel','cworker']


class storloginline(object):
    model = storelog
    extra = 1

class storeAdmin(object):
    list_display = ['pk','num','area','typeskey','locationkey','address','customertel','Dateofaudit','status','designerkey','managerkey','companykey']
    list_filter = ['designerkey']
    search_fields = ['num','area','types']

    inlines = [storloginline]

class storelogAdmin(object):
    list_display = ['storekey','logtypekey','log','date']
    list_filter = ['storekey__num','logtypekey__lname','log','date']
    search_fields = ['storekey','logtypekey','date','log']

class supportslogAdmin(object):
    list_display = ['store','description','type']
    list_filter = ['store__name','type','store']
    search_fields = ['store__name','description']


class infoslogAdmin(object):
    list_display = ['store','info']
    list_filter = ['store__name','info']
    search_fields = ['store__name','info']

class picsAdmin(object):
    list_display = ['store','info']
    list_filter = ['store__name','info']
    search_fields = ['store__name','info']



xadmin.site.register(company,companyAdmin)

xadmin.site.register(types)
xadmin.site.register(location)
xadmin.site.register(logtype)
xadmin.site.register(storelog,storelogAdmin)
xadmin.site.register(Store,storeAdmin)

xadmin.site.register(pics,picsAdmin)
xadmin.site.register(infos,infoslogAdmin)
xadmin.site.register(supports,supportslogAdmin)



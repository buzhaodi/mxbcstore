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



xadmin.site.register(company,companyAdmin)

xadmin.site.register(types)
xadmin.site.register(location)
xadmin.site.register(logtype)
xadmin.site.register(storelog,storelogAdmin)
xadmin.site.register(Store,storeAdmin)



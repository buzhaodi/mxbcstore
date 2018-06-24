from django.db import models

# Create your models here.
# 装修公司模型
class company(models.Model):
    class Meta:
        verbose_name_plural = '装修公司'

    def __str__(self):
        return self.cname

    cname = models.CharField(max_length=10, verbose_name='公司名称')
    cworker = models.CharField(max_length=10, verbose_name='工头名称')
    ctel = models.CharField(max_length=20, verbose_name='电话')


# 类型模型
class types(models.Model):
    class Meta:
        verbose_name_plural = '类型'

    def __str__(self):
        return self.tname

    tname = models.CharField(max_length=10, verbose_name='类型')


# 线路模型
class location(models.Model):
    class Meta:
        verbose_name_plural = '线路'

    def __str__(self):
        return self.lname

    lname = models.CharField(max_length=10, verbose_name='线路')


# 日志类型模型
class logtype(models.Model):
    class Meta:
        verbose_name_plural = '日志类型'

    def __str__(self):
        return str(self.lname)

    lname = models.CharField(max_length=10, verbose_name='日志类型')


class Store(models.Model):
    class Meta:
        verbose_name_plural = '门店'

    def __str__(self):
        return str(self.name)

    num = models.IntegerField(verbose_name='门牌编号')
    area = models.CharField(max_length=20, verbose_name='面积')
    address = models.CharField(max_length=400, verbose_name='地址')
    customertel = models.CharField(max_length=40, verbose_name='客户电话')
    Dateofaudit = models.DateTimeField(verbose_name='审核日期', null=True, blank=True)
    status = models.CharField(max_length=40, verbose_name='店面状态', null=True, blank=True)

    locationkey = models.ForeignKey(location, on_delete=models.CASCADE, verbose_name='线路')
    typeskey = models.ForeignKey(types, on_delete=models.CASCADE, verbose_name='类型')
    designerkey = models.ForeignKey("user.UserProfile", on_delete=models.CASCADE, verbose_name='设计师',related_name='design_name', null=True, blank=True)
    managerkey = models.ForeignKey("user.UserProfile", on_delete=models.CASCADE, verbose_name='监理',related_name='manager_name', null=True, blank=True)
    companykey = models.ForeignKey(company, on_delete=models.CASCADE, verbose_name='公司', null=True, blank=True)
    avatar=models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100,verbose_name='店面头像')
    bulletin=models.CharField(max_length=400,verbose_name='店面描述', null=True, blank=True)
    deliveryTime=models.IntegerField(verbose_name='平均出餐时长', null=True, blank=True)
    description=models.CharField(max_length=50,verbose_name='店面简单描述', null=True, blank=True)
    foodScore=models.CharField(max_length=10,verbose_name='商品评分',default='5')
    serviceScore=models.CharField(max_length=10,verbose_name='服务评分',default='5')
    score=models.CharField(max_length=10,verbose_name='店面评分',default='5')
    rankRate=models.CharField(max_length=10,verbose_name='高于其他店面',default='95.0')
    sellCount=models.IntegerField(verbose_name='共售',default=0)
    deliveryPrice=models.IntegerField(verbose_name='商家配送',default=1)
    minPrice=models.CharField(max_length=10,verbose_name='起点价格',default='10')
    name=models.CharField(max_length=50,verbose_name='店名',default='密雪冰城新店')


class infos(models.Model):
    class Meta:
        verbose_name_plural = '门店信息'

    def __str__(self):
        return str(self.store)
    store=models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='门店')
    info=models.CharField(max_length=50,verbose_name='信息')


class supports(models.Model):
    class Meta:
        verbose_name_plural = '活动'

    def __str__(self):
        return str(self.store)
    store=models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='门店')
    description=models.CharField(max_length=50,verbose_name='活动')
    type = models.IntegerField(verbose_name='类型')


class pics(models.Model):
    class Meta:
        verbose_name_plural = '门店照片'

    def __str__(self):
        return str(self.store)
    store=models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='门店')
    info=models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100,verbose_name='店面照片')


class storelog(models.Model):
    class Meta:
        verbose_name_plural = '店面日志'

    storekey = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='店面')
    logtypekey = models.ForeignKey(logtype, on_delete=models.CASCADE, verbose_name='日志类型')
    log = models.CharField(max_length=20, verbose_name='日志', null=True, blank=True)
    date = models.DateTimeField(verbose_name='记录日期', auto_now_add=True)
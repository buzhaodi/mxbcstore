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
        return str(self.num)

    num = models.IntegerField(verbose_name='门牌编号')
    area = models.CharField(max_length=20, verbose_name='面积')
    address = models.CharField(max_length=400, verbose_name='地址')
    customertel = models.CharField(max_length=40, verbose_name='客户电话')
    Dateofaudit = models.DateTimeField(verbose_name='审核日期', null=True, blank=True)
    status = models.CharField(max_length=40, verbose_name='店面状态', null=True, blank=True)

    locationkey = models.ForeignKey(location, on_delete=models.CASCADE, verbose_name='线路')
    typeskey = models.ForeignKey(types, on_delete=models.CASCADE, verbose_name='类型')
    designerkey = models.ForeignKey("user.UserProfile", on_delete=models.CASCADE, verbose_name='设计师',related_name='design_name')
    managerkey = models.ForeignKey("user.UserProfile", on_delete=models.CASCADE, verbose_name='监理',related_name='manager_name')
    companykey = models.ForeignKey(company, on_delete=models.CASCADE, verbose_name='公司')


class storelog(models.Model):
    class Meta:
        verbose_name_plural = '店面日志'

    storekey = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='店面')
    logtypekey = models.ForeignKey(logtype, on_delete=models.CASCADE, verbose_name='日志类型')
    log = models.CharField(max_length=20, verbose_name='日志', null=True, blank=True)
    date = models.DateTimeField(verbose_name='记录日期', auto_now_add=True)
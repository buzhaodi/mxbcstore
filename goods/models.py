from django.db import models

# Create your models here.
class types(models.Model):
    class Meta:
        verbose_name_plural = '种类'
    def __str__(self):
        return str(self.name)
    name=models.CharField(max_length=50,verbose_name='分类名称')
    type = models.CharField(choices=(("-1", u"普通"), ("2", u"特价"), ("1", u"折扣")), default="-1", max_length=5,verbose_name='是否折扣')



class goods(models.Model):
    class Meta:
        verbose_name_plural = '产品'
    def __str__(self):
        return str(self.name)


    type=models.ForeignKey(types, on_delete=models.CASCADE, verbose_name='分类')
    name=models.CharField(max_length=50,verbose_name='产品名称')
    price=models.CharField(max_length=50,verbose_name='产品现价')
    oldprice=models.CharField(max_length=50,verbose_name='产品原价')
    description=models.CharField(max_length=200,verbose_name='描述')
    sellCount=models.IntegerField(verbose_name='销量')
    rating=models.IntegerField(verbose_name='排行')
    info=models.CharField(max_length=400,verbose_name='详情')
    icon = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100, verbose_name='小图',null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100,verbose_name='大图',null=True,blank=True)
    stores=models.ManyToManyField(
        'store.Store',
        verbose_name='可售店面',
        blank=True,
    )




class ratings(models.Model):
    class Meta:
        verbose_name_plural = '评价'
    def __str__(self):
        return str(self.user)
    user=models.ForeignKey("user.UserProfile",on_delete=models.CASCADE, verbose_name='用户名')
    time=models.DateTimeField(auto_now=True,verbose_name='评论时间')
    rateType=models.CharField(choices=(("1",u"差评"),("0",u"好评")),default="0",max_length=5)
    text=models.CharField(max_length=400,verbose_name='评论内容')
    avatar = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100,verbose_name='头像')
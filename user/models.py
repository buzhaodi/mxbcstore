from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name= models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birday=models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender= models.CharField(choices=(("male",u"男"),("female",u"女")),default="female",max_length=10)
    address=models.CharField(max_length=100,default="",verbose_name='地址')
    mobile=models.CharField(max_length=11,null=True,blank=True,verbose_name='电话')
    image=models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100,verbose_name='头像')
    openid=models.CharField(max_length=100,default="",verbose_name='微信openid')


    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.username
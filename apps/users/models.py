from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime

# Create your models here.




class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=7, choices=(('male', u'男'), ('female', u'女')), default='male')
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)
    about = models.TextField(verbose_name=u'关于我', default='')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(verbose_name='验证码类型', choices=(('register', u'注册'), ('forget', u'找回密码')), max_length=10)
    send_time = models.DateTimeField(verbose_name='发送时间', default=timezone.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name


    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)

class UserPrefer(models.Model):
    user = models.OneToOneField(UserProfile, models.DO_NOTHING, primary_key=True)
    t2_t1 = models.CharField(db_column='T2_T1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    l_t1 = models.CharField(db_column='L_T1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    e_t1 = models.CharField(db_column='E_T1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    h_t1 = models.CharField(db_column='H_T1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g_t1 = models.CharField(db_column='G_T1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v1_t1 = models.CharField(db_column='V1_T1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v2_t1 = models.CharField(db_column='V2_T1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    l_t2 = models.CharField(db_column='L_T2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    e_t2 = models.CharField(db_column='E_T2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    h_t2 = models.CharField(db_column='H_T2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g_t2 = models.CharField(db_column='G_T2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v1_t2 = models.CharField(db_column='V1_T2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v2_t2 = models.CharField(db_column='V2_T2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    e_l = models.CharField(db_column='E_L', max_length=20, blank=True, null=True)  # Field name made lowercase.
    h_l = models.CharField(db_column='H_L', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g_l = models.CharField(db_column='G_L', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v1_l = models.CharField(db_column='V1_L', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v2_l = models.CharField(db_column='V2_L', max_length=20, blank=True, null=True)  # Field name made lowercase.
    h_e = models.CharField(db_column='H_E', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g_e = models.CharField(db_column='G_E', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v1_e = models.CharField(db_column='V1_E', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v2_e = models.CharField(db_column='V2_E', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g_h = models.CharField(db_column='G_H', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v1_h = models.CharField(db_column='V1_H', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v2_v1 = models.CharField(db_column='V2_V1', max_length=20, blank=True, null=True)
    v1_g = models.CharField(db_column='V1_G', max_length=20, blank=True, null=True)  # Field name made lowercase.
    v2_g = models.CharField(db_column='V2_G', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    v2_h = models.CharField(db_column='V2_H', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_prefer'



class UserWeight(models.Model):
    weight_t1 = models.FloatField()
    weight_t2 = models.FloatField()
    weight_v1 = models.FloatField()
    weight_v2 = models.FloatField()
    weight_g = models.FloatField()
    weight_l = models.FloatField()
    weight_h = models.FloatField()
    weight_e = models.FloatField()
    user = models.OneToOneField(UserProfile, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_weight'
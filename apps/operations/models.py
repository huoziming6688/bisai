from django.db import models
from users.models import *
from houses.models import *
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    hid = models.CharField(max_length=15)
    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name
        db_table = 'userfav'
# Create your models here.

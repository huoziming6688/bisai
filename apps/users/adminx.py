# _*_ encoding:utf-8 _*_
__author__ = '595'
__date__ = '2019/3/5 21:36'
import xadmin

from .models import *
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '住哪儿网后台'
    site_footer = '住哪儿'
    menu_style = 'accordion'


# class UserProfileAdmin(object):
#     list_display = ['nick_name', 'birthday', 'gender', 'address','mobile', 'image']
#     search_fields = ['nick_name', 'birthday', 'gender', 'address','mobile', 'image']
#     list_filter = ['nick_name', 'birthday', 'gender', 'address','mobile', 'image']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
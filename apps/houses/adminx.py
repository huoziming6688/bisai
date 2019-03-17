# _*_ encoding:utf-8 _*_
__author__ = '595'
__date__ = '2019/3/5 21:44'

import xadmin

from .models import *


class HouseAdmin(object):
    list_display = ['hid', 'hyuanid', 'htitle', 'himageurl','hurl', 'subdistrictid', 'himagedir']
    search_fields = ['hid', 'hyuanid', 'htitle', 'himageurl','hurl', 'subdistrictid', 'himagedir']
    list_filter = ['hid', 'hyuanid', 'htitle', 'himageurl','hurl', 'subdistrictid', 'himagedir']


class HouseDetailAdmin(object):
    list_display = ['hid', 'hprice', 'hdirection', 'htype','harea', 'hfloor', 'hpubdate', 'hcontact_info', 'description']
    search_fields = ['hid', 'hprice', 'hdirection', 'htype','harea', 'hfloor', 'hpubdate', 'hcontact_info', 'description']
    list_filter = ['hid', 'hprice', 'hdirection', 'htype','harea', 'hfloor', 'hpubdate', 'hcontact_info', 'description']


xadmin.site.register(House, HouseAdmin)
xadmin.site.register(HouseDetail, HouseDetailAdmin)
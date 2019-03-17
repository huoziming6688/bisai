# _*_ encoding:utf-8 _*_
__author__ = '595'
__date__ = '2019/3/5 20:51'

import xadmin

from .models import *


class ProvinceAdmin(object):
    list_display = ['pid', 'provincename']
    search_fields = ['pid', 'provincename']
    list_filter = ['pid', 'provincename']


class CityAdmin(object):
    list_display = ['cid', 'cityname', 'provinceid']
    search_fields = ['cid', 'cityname', 'provinceid']
    list_filter = ['cid', 'cityname', 'provinceid']


class DistrictAdmin(object):
    list_display = ['did', 'cdistrictname', 'cityid']
    search_fields = ['did', 'cdistrictname', 'cityid']
    list_filter = ['did', 'districtname', 'cityid']


class SubdistrictAdmin(object):
    list_display = ['sid', 'yuanid', 'sname', 'url','imageurl', 'districtid', 'issearch', 'page', 'imagedir']
    search_fields = ['sid', 'yuanid', 'sname', 'url','imageurl', 'districtid', 'issearch', 'page', 'imagedir']
    list_filter = ['sid', 'yuanid', 'sname', 'url','imageurl', 'districtid', 'issearch', 'page', 'imagedir']


class SubdistrictLocationAdmin(object):
    list_display = ['sid', 'jingdu', 'weidu']
    search_fields = ['sid', 'jingdu', 'weidu']
    list_filter = ['sid', 'jingdu', 'weidu']


class SubdistrictDetailAdmin(object):
    list_display = ['sid', 'avg_price', 'built_time', 'built_type','manage_fee', 'manage_company', 'developer', 'total_buildings', 'total_houses']
    search_fields = ['sid', 'avg_price', 'built_time', 'built_type','manage_fee', 'manage_company', 'developer', 'total_buildings', 'total_houses']
    list_filter = ['sid', 'avg_price', 'built_time', 'built_type','manage_fee', 'manage_company', 'developer', 'total_buildings', 'total_houses']


xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(City, CityAdmin)
xadmin.site.register(District, DistrictAdmin)
xadmin.site.register(Subdistrict, SubdistrictAdmin)
xadmin.site.register(SubdistrictLocation, SubdistrictLocationAdmin)
xadmin.site.register(SubdistrictDetail, SubdistrictDetailAdmin)
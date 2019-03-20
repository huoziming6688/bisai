from django.shortcuts import render,redirect
from django.template.response import TemplateResponse
from django.views.generic.base import View
# from .forms import SearchForm
from django.http import JsonResponse
from subdistricts.models import *
from houses.models import *
from users.models import UserProfile
from django.db.models import Q
# Create your views here.
import json
from django.db.models import Sum
#改动了views prolist 和urls


def showrent(request):
    return render(request, 'properties-list.html')

def getinfo(request):
        get = request.GET
        select_bedrooms = get['select-bedrooms']
        price = get['price']

        price = price.replace('¥', '')
        price = price.replace(' ', '')
        price = price.split('-')
        min_price = int(price[0])
        max_price = int(price[1])
        a = select_bedrooms[0]
        if a == '一':
            a = '1室'
        elif a == '二':
            a = '2室'
        elif a == '三':
            a = '3室'
        elif a == '四':
            a = '4室'
        xiaoqulist = []
        for xiaoqu in Subdistrict.objects.filter(house__housedetail__hprice__gte=min_price,house__housedetail__hprice__lte=max_price,house__housedetail__htype__contains=a).distinct()[::10]:
            xiaoquinfo = dict()
            xiaoquinfo['housecount']=xiaoqu.house_set.filter(housedetail__hprice__gte=min_price,housedetail__hprice__lte=max_price,housedetail__htype__contains=a).count()
            xiaoquinfo['sid']=xiaoqu.sid
            xiaoquinfo['avgprice']=round(xiaoqu.house_set.filter(housedetail__hprice__gte=min_price, housedetail__hprice__lte=max_price,
                                    housedetail__htype__contains=a).aggregate(totalprict=Sum('housedetail__hprice'))['totalprict']/xiaoquinfo['housecount'])
            xiaoquinfo['sname']=xiaoqu.sname
            xiaoquinfo['built_time']=xiaoqu.subdistrictdetail.built_time
            xiaoquinfo['address']=xiaoqu.subdistrictdetail.subaddress
            xiaoquinfo['jingdu']=xiaoqu.subdistrictlocation.jingdu
            xiaoquinfo['weidu']=xiaoqu.subdistrictlocation.weidu
            xiaoqulist.append(xiaoquinfo)

        return JsonResponse(xiaoqulist,safe=False)




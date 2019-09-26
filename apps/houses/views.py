from django.shortcuts import render
from django.views.generic import View
from .models import House, HouseDetail,HouseFacility
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from subdistricts.models import Subdistrict
from operations.views import *
# Create your views here.
import json

class Houseinfo(View):
    def get(self, request,sid):
        houseinfolist=[]
        subdistrict=Subdistrict.objects.get(sid=sid)
        sname=subdistrict.sname

        try:
            get = request.GET
            select_bedrooms = get['select_bedrooms']
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
            houseset=subdistrict.house_set.filter(housedetail__hprice__gte=min_price,housedetail__hprice__lte=max_price,housedetail__htype__contains=a).all()
        except:
            houseset=subdistrict.house_set.all()
        for house in houseset:
            houseinfo = dict()
            houseinfo['hid'] = house.hid
            houseinfo['sid'] = house.subdistrictid
            houseinfo['htitle']=house.htitle
            houseinfo['hurl'] = house.hurl
            houseinfo['hprice']=house.housedetail.hprice
            houseinfo['hpredictprice']=house.housedetail.hpredictprice
            houseinfo['hdirection']=house.housedetail.hdirection
            houseinfo['htype']=house.housedetail.htype
            houseinfo['harea']=house.housedetail.harea
            houseinfo['hfloor'] = house.housedetail.hfloor
            houseinfo['hpubdate'] = house.housedetail.hpubdate
            houseinfo['hcontact_info'] = house.housedetail.hcontact_info
            houseinfo['description'] = house.housedetail.description.replace('<br />','')
            houseinfolist.append(houseinfo)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(houseinfolist, 5, request=request)

        house = p.page(page)
        return render(request, 'house-list.html', {
            'house': house,
            'sname':sname,
            'sid':sid,
        })


class ShowHouseDetail(View):
    # 房源详情页
    def get(self, request, hid):
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, hid=hid):
                has_fav = True
        housedetail = HouseDetail.objects.get(hid=hid)
        housefacility=HouseFacility.objects.get(hid=hid)
        sid = housedetail.hid.subdistrictid
        hid = housedetail.hid
        hprice = housedetail.hprice
        hpredictprice = housedetail.hpredictprice
        hdirection = housedetail.hdirection
        harea = housedetail.harea
        room_nums = housedetail.htype[0]
        toilet_nums = housedetail.htype[4]
        description = housedetail.description
        des = description.replace('<br />', '')
        des_final = des.replace('。', '')
        contact = housedetail.hcontact_info
        title = housedetail.hid.htitle
        district=housedetail.hid.subdistrictid.districtid.districtname
        jingdu=housedetail.hid.subdistrictid.subdistrictlocation.jingdu
        weidu=housedetail.hid.subdistrictid.subdistrictlocation.weidu
        return render(request, 'house-detail.html', {
            'sid': sid,
            'hid': hid,
            'hprice': hprice,
            'hdirection': hdirection,
            'harea': harea,
            'room_nums': room_nums,
            'toilet_nums': toilet_nums,
            'des_final': des_final,
            'contact': contact,
            'title': title,
            'district':district,
            'housefacility':housefacility,
            'jingdu':json.dumps(jingdu),
            'weidu':json.dumps(weidu),
            'has_fav':has_fav,
            'hpredictprice':hpredictprice
        })




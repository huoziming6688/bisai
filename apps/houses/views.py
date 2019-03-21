from django.shortcuts import render
from django.views.generic import View
from .models import House, HouseDetail
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from subdistricts.models import Subdistrict
# Create your views here.


class Houseinfo(View):
    def get(self, request,sid):
        houseinfolist=[]
        subdistrict=Subdistrict.objects.get(sid=sid)
        sname=subdistrict.sname
        for house in subdistrict.house_set.all():
            houseinfo = dict()
            houseinfo['hid'] = house.hid
            houseinfo['sid'] = house.subdistrictid
            houseinfo['htitle']=house.htitle
            houseinfo['hurl'] = house.hurl
            houseinfo['hprice']=house.housedetail.hprice
            houseinfo['hdirection']=house.housedetail.hdirection
            houseinfo['htype']=house.housedetail.htype
            houseinfo['harea']=house.housedetail.harea
            houseinfo['hfloor'] = house.housedetail.hfloor
            houseinfo['hpubdate'] = house.housedetail.hpubdate
            houseinfo['hcontact_info'] = house.housedetail.hcontact_info
            houseinfo['description'] = house.housedetail.description
            houseinfolist.append(houseinfo)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(houseinfolist, 5, request=request)

        house = p.page(page)
        return render(request, 'house-list.html', {
            'house': house,'sname':sname,
        })


class ShowHouseDetail(View):
    # 房源详情页
    def get(self, request, hid):
        housedetail = HouseDetail.objects.get(hid=hid)
        sid = housedetail.hid.subdistrictid
        hid = housedetail.hid
        hprice = housedetail.hprice
        hdirection = housedetail.hdirection
        harea = housedetail.harea
        room_nums = housedetail.htype[0]
        toilet_nums = housedetail.htype[4]
        description = housedetail.description
        des = description.replace('<br />', '')
        des_final = des.replace('。', '')
        contact = housedetail.hcontact_info
        title = housedetail.hid.htitle
        return render(request, 'property-single-slider.html', {
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
        })




from django.shortcuts import render
from django.views.generic import View
from .models import Subdistrict, SubdistrictDetail
from houses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class xiaoquview(View):
    def get(self, request):

        xiaoquinfolist=[]
        for xiaoqu in SubdistrictDetail.objects.all():
            xiaoquinfo = dict()
            xiaoquinfo['housecount']=xiaoqu.sid.house_set.count()
            xiaoquinfo['sname']=xiaoqu.sid.sname
            xiaoquinfo['imageurl']=xiaoqu.sid.imageurl
            xiaoquinfo['sid']=xiaoqu.sid.sid
            xiaoquinfo['address']=xiaoqu.subaddress
            xiaoquinfo['built_time']=xiaoqu.built_time
            xiaoquinfo['avg_price'] = 0
            for house in xiaoqu.sid.house_set.all():
                xiaoquinfo['avg_price'] += house.housedetail.hprice
            if xiaoquinfo['housecount']:
                xiaoquinfo['avg_price']=round(xiaoquinfo['avg_price']/xiaoquinfo['housecount'])
            xiaoquinfolist.append(xiaoquinfo)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(xiaoquinfolist, 5, request=request)

        xq = p.page(page)
        return render(request, 'agency-list.html', {
            'xiaoqu': xq,
        })


from django.shortcuts import render
from django.views.generic import View
from .models import Subdistrict, SubdistrictDetail
from houses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.db.models import Sum

class xiaoquview(View):
    def get(self, request):

        xiaoquinfolist=[]
        for xiaoqu in SubdistrictDetail.objects.all()[:500]:
            xiaoquinfo = dict()
            xiaoquinfo['housecount']=xiaoqu.sid.house_set.count()
            print(xiaoquinfo['housecount'])
            xiaoquinfo['sname']=xiaoqu.sid.sname
            xiaoquinfo['imageurl']=xiaoqu.sid.imageurl
            xiaoquinfo['sid']=xiaoqu.sid.sid
            xiaoquinfo['address']=xiaoqu.subaddress
            xiaoquinfo['built_time']=xiaoqu.built_time
            print(xiaoqu.sid)
            if xiaoquinfo['housecount'] :
                 xiaoquinfo['avg_price'] = round(int(xiaoqu.sid.house_set.all().aggregate(totalprice=Sum('housedetail__hprice'))['totalprice'])/xiaoquinfo['housecount'])
            else:xiaoquinfo['avg_price']=0
            if xiaoquinfo['housecount']:
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


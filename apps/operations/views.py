from django.shortcuts import render,redirect,HttpResponse
from django.template.response import TemplateResponse
from django.views.generic.base import View
# from .forms import SearchForm
from django.http import JsonResponse
from subdistricts.models import *
from houses.models import *
from users.models import UserProfile
from django.db.models import Q
# Create your views here.
from operations.models import *
from django.db.models import Sum
#改动了views prolist 和urls
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

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
            if str(xiaoqu.imageurl)=='':

                xiaoquinfo['hasimage']=0
            else:
                xiaoquinfo['hasimage']=1

            # print(xiaoquinfo['hasimage'])
            xiaoqulist.append(xiaoquinfo)
            # print(xiaoqulist)
        return JsonResponse(xiaoqulist,safe=False)


class UserCenterView(View):
    #@method_decorator(login_required)
    def get(self, request):
        return render(request, 'user-profile.html', {})


class AddfavView(View):
    # @method_decorator(login_required)
    def post(self, request):
        hid = request.POST.get('hid', '')
        if not request.user.is_authenticated:
            return render(request, 'login.html', {})
        exist_records = UserFavorite.objects.filter(user=request.user, hid=hid)
        if exist_records:
            exist_records.delete()
            return HttpResponse('{"status":"fail", "msg":"取消收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            user_fav.user = request.user
            user_fav.hid = hid
            user_fav.save()
            return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')


class ShowFavView(View):
    # @method_decorator(login_required)
    def get(self, request):
        favhouse = []
        if not request.user.is_authenticated:
            return render(request, 'favourite-properties.html')
        for house in UserFavorite.objects.filter(user=request.user):
            for schousedetail in HouseDetail.objects.filter(hid=house.hid):
                schouse_1 = dict()
                schouse_1['hprice'] = schousedetail.hprice
                schouse_1['himagedir'] = schousedetail.hid.himagedir
                schouse_1['harea'] = schousedetail.harea
                schouse_1['sid'] = schousedetail.hid.subdistrictid
                schouse_1['hid'] = schousedetail.hid
                schouse_1['htitle'] = schousedetail.hid.htitle
                schouse_1['htype'] = schousedetail.htype
                schouse_1['contact'] = schousedetail.hcontact_info
                favhouse.append(schouse_1)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(favhouse, 5, request=request)
        favhouse = p.page(page)
        return render(request, 'favourite-properties.html', {
                'favhouse': favhouse,
        })


class DeleteFavView(View):
    def get(self, request, hid):
        del_record = UserFavorite.objects.filter(hid=hid)
        del_record.delete()
        return HttpResponseRedirect('/shoucang')
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
import numpy as np

def get_w(array):
    RI_dict = {1: 0, 2: 0, 3: 0.52, 4: 0.89, 5: 1.12,
               6: 1.24, 7: 1.36, 8: 1.41, 9: 1.46, 10: 1.52}
    # 1、计算出阶数 看这个数组是几维的 也就是后面对应字典查询！
    row = array.shape[0]
    # 2、按列求和
    a_axis_0_sum = array.sum(axis=0)
    # 3、得到新的矩阵b 就是把每一个数都除以列和
    b = array / a_axis_0_sum
    # 4、计算新矩阵b行和
    b_axis_1_sum = b.sum(axis=1)
    # 5、将b_axis_1_sum每一个值除以总和
    W = b_axis_1_sum / sum(b_axis_1_sum)
    # 6、将原始矩阵乘以W
    a_W = np.dot(array, W)
    # 7、求解最大特征值
    lambda_max = 0
    for i in range(len(a_W)):
        lambda_max += (a_W[i] / W[i])
    lambda_max = lambda_max / len(a_W)  # 求最大特征值
    # 8、检验判断矩阵的一致性
    C_I = (lambda_max - row) / (row - 1)
    R_I = RI_dict[row]
    C_R = C_I / R_I
    if C_R < 0.1:
        return W,C_I,R_I,C_R
    else:
        print('矩阵 %s 一致性检验未通过，需要重新进行调整判断矩阵' % (array))







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

def showpianhao(request):
    if not request.user.is_authenticated:
        return render(request, 'user_pianhao.html')
    else:
        userpianhao=UserPrefer.objects.get(user_id=request.user)
        pianhaodict={'t2_t1':userpianhao.t2_t1,
        'l_t1':userpianhao.l_t1,
        'e_t1':userpianhao.e_t1,
        'h_t1':userpianhao.h_t1,
        'g_t1':userpianhao.g_t1,
        'v1_t1':userpianhao.v1_t1,
        'v2_t1':userpianhao.v2_t1,
        'l_t2':userpianhao.l_t2,
        'e_t2':userpianhao.e_t2,
        'h_t2':userpianhao.h_t2,
        'g_t2':userpianhao.g_t2,
        'v1_t2':userpianhao.v1_t2,
        'v2_t2':userpianhao.v2_t2,
        'e_l':userpianhao.e_l,
        'h_l':userpianhao.h_l,
        'g_l':userpianhao.g_l,
        'v1_l':userpianhao.v1_l,
        'v2_l':userpianhao.v2_l,
        'h_e':userpianhao.h_e,
        'g_e':userpianhao.g_e,
        'v1_e':userpianhao.v1_e,
        'v2_e':userpianhao.v2_e,
        'g_h':userpianhao.g_h,
        'v1_h':userpianhao.v1_h,
        'v2_h':userpianhao.v2_h,
        'v1_g':userpianhao.v1_g,
        'v2_g':userpianhao.v2_g,
        'v2_v1':userpianhao.v2_v1,
        'selectlist': ['1', '2', '3', '4', '5', '1/2', '1/3', '1/4', '1/5']}
        return render(request,'user_pianhao.html',pianhaodict)


def setpianhao(request):
    POST = request.POST
    userpianhao=UserPrefer()
    userpianhao.user_id=request.user
    userpianhao.t2_t1=POST['t2_t1']
    userpianhao.l_t1=POST['l_t1']
    userpianhao.e_t1=POST['e_t1']
    userpianhao.h_t1=POST['h_t1']
    userpianhao.g_t1=POST['g_t1']
    userpianhao.v1_t1=POST['v1_t1']
    userpianhao.v2_t1=POST['v2_t1']
    userpianhao.l_t2=POST['l_t2']
    userpianhao.e_t2=POST['e_t2']
    userpianhao.h_t2=POST['h_t2']
    userpianhao.g_t2=POST['g_t2']
    userpianhao.v1_t2=POST['v1_t2']
    userpianhao.v2_t2=POST['v2_t2']
    userpianhao.e_l=POST['e_l']
    userpianhao.h_l=POST['h_l']
    userpianhao.g_l=POST['g_l']
    userpianhao.v1_l=POST['v1_l']
    userpianhao.v2_l=POST['v2_l']
    userpianhao.h_e=POST['h_e']
    userpianhao.g_e=POST['g_e']
    userpianhao.v1_e=POST['v1_e']
    userpianhao.v2_e=POST['v2_e']
    userpianhao.g_h=POST['g_h']
    userpianhao.v1_h=POST['v1_h']
    userpianhao.v2_h=POST['v2_h']
    userpianhao.v1_g=POST['v1_g']
    userpianhao.v2_g=POST['v2_g']
    userpianhao.v2_v1=POST['v2_v1']
    userpianhao.save()
    userweight = UserWeight()
    userweight.user=request.user
    array = np.ones([8, 8])
    a=POST['t2_t1']
    array[1][0] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['l_t1']
    array[2][0] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['l_t2']
    array[2][1] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['e_t1']
    array[3][0] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['e_t2']
    array[3][1] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['e_l']
    array[3][2] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['h_t1']
    array[4][0] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['h_t2']
    array[4][1] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['h_l']
    array[4][2] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['h_e']
    array[4][3] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['g_t1']
    array[5][0] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['g_t2']
    array[5][1] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['g_l']
    array[5][2] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['g_e']
    array[5][3] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['g_h']
    array[5][4] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v1_t1']
    array[6][0] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v1_t2']
    array[6][1] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v1_l']
    array[6][2] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v1_e']
    array[6][3] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v1_h']
    array[6][4] = float(a) if a.find('/') == -1 else int(a.split('/')[0]) / int(a.split('/')[1])
    a = POST['v1_g']
    array[6][5] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v2_t1']
    array[7][0] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v2_t2']
    array[7][1] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v2_l']
    array[7][2] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v2_e']
    array[7][3] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v2_h']
    array[7][4] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v2_g']
    array[7][5] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    a = POST['v2_v1']
    array[7][6] = float(a) if a.find('/')==-1 else int(a.split('/')[0])/int(a.split('/')[1])
    for i in range(0, 8):
        for j in range(i, 8):
            array[i][j] = (1 / array.T)[i][j]
    W=get_w(array)[0]
    userweight.weight_t1=W[0]
    userweight.weight_t2=W[1]
    userweight.weight_l=W[2]
    userweight.weight_e=W[3]
    userweight.weight_h=W[4]
    userweight.weight_g=W[5]
    userweight.weight_v1=W[6]
    userweight.weight_v2=W[7]
    userweight.save()
    return redirect('/pianhao')
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
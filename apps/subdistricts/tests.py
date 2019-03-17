from django.test import TestCase
from .models import SubdistrictDetail,Subdistrict
class test1(TestCase):
    def test_1(self):
        xiaoquinfo = dict()
        xiaoquinfolist = []
        for xiaoqu in SubdistrictDetail.objects.all():
            xiaoquinfo['housecount'] = xiaoqu.sid.house_set.count()
            xiaoquinfo['sname'] = xiaoqu.sid.sname
            xiaoquinfo['imageurl'] = xiaoqu.sid.imageurl
            xiaoquinfo['sid'] = xiaoqu.sid
            xiaoquinfolist.append(xiaoquinfo)
            print(xiaoquinfolist)
# Create your tests here.

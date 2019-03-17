from __future__ import unicode_literals

# Create your models here.

from django.db import models


class Province(models.Model):
    pid = models.CharField(primary_key=True, max_length=2)
    provincename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'省份信息'
        verbose_name_plural = verbose_name
        db_table = 'province'

    def __str__(self):
        return self.pid


class City(models.Model):
    cid = models.CharField(primary_key=True, max_length=4)
    cityname = models.CharField(max_length=255, blank=True, null=True)
    provinceid = models.ForeignKey('Province', db_column='provinceid', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'城市信息'
        verbose_name_plural = verbose_name
        db_table = 'city'

    def __str__(self):
        return self.cid

class District(models.Model):
    did = models.CharField(primary_key=True, max_length=6)
    districtname = models.CharField(max_length=255, blank=True, null=True)
    cityid = models.ForeignKey(City, db_column='cityid', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'区信息'
        verbose_name_plural = verbose_name
        db_table = 'district'

    def __str__(self):
        return self.did

class Subdistrict(models.Model):
    sid = models.CharField(primary_key=True, max_length=11)
    yuanid = models.CharField(max_length=255)
    sname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    url = models.CharField(unique=True, max_length=255, blank=True, null=True)
    imageurl = models.ImageField(upload_to='image/subdistrict/%Y/%m', max_length=255, blank=True, null=True)
    districtid = models.ForeignKey(District, db_column='districtid', blank=True, null=True, on_delete=models.CASCADE)
    issearch = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    imagedir = models.ImageField(upload_to='subdistrict/%Y/%m',max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'小区信息'
        verbose_name_plural = verbose_name
        db_table = 'subdistrict'

    def __str__(self):
        return self.sid


class SubdistrictLocation(models.Model):
    sid = models.OneToOneField(Subdistrict, db_column='sid', primary_key=True, on_delete=models.CASCADE)
    jingdu = models.CharField(max_length=255, blank=True, null=True)
    weidu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'小区位置'
        verbose_name_plural = verbose_name
        db_table = 'subdistrict location'

    def __str__(self):
        return self.sid


class SubdistrictDetail(models.Model):
    sid = models.OneToOneField(Subdistrict, db_column='sid', primary_key=True, on_delete=models.CASCADE)
    avg_price = models.FloatField(blank=True, null=True)
    built_time = models.CharField(max_length=255, blank=True, null=True)
    built_type = models.CharField(max_length=255, blank=True, null=True)
    manage_fee = models.CharField(max_length=255, blank=True, null=True)
    manage_company = models.CharField(max_length=255, blank=True, null=True)
    developer = models.CharField(max_length=255, blank=True, null=True)
    total_buildings = models.CharField(max_length=255, blank=True, null=True)
    total_houses = models.CharField(max_length=255, blank=True, null=True)
    subaddress = models.CharField(max_length=255, blank=True, null=True)
    class Meta:

        verbose_name = u'小区详情'
        verbose_name_plural = verbose_name
        db_table = 'subdistrict_detail'

    def __str__(self):
        return self.sid
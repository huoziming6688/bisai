from __future__ import unicode_literals
from django.db import models
from subdistricts.models import Subdistrict
# Create your models here.


class House(models.Model):
    hid = models.CharField(primary_key=True, max_length=15)
    hyuanid = models.CharField(max_length=255, blank=True, null=True)
    htitle = models.TextField(blank=True, null=True)
    hsmallimageurl = models.CharField(max_length=255, blank=True, null=True)
    hurl = models.CharField(max_length=255, blank=True, null=True)
    subdistrictid = models.ForeignKey(Subdistrict, on_delete=models.CASCADE, db_column='subdistrictid', blank=True, null=True)
    himagedir = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'房子信息'
        verbose_name_plural = verbose_name
        db_table = 'house'

    def __str__(self):
        return self.hid


class HouseDetail(models.Model):
    hid = models.OneToOneField(House, on_delete=models.CASCADE, db_column='hid', primary_key=True)
    hprice = models.IntegerField(blank=True, null=True)
    hdirection = models.CharField(max_length=255, blank=True, null=True)
    htype = models.CharField(max_length=255, blank=True, null=True)
    harea = models.IntegerField(blank=True, null=True)
    hfloor = models.CharField(max_length=255, blank=True, null=True)
    hpubdate = models.CharField(max_length=255, blank=True, null=True)
    hcontact_info = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = u'房子详细'
        verbose_name_plural = verbose_name
        db_table = 'house_detail'

    def __str__(self):
        return self.hid
# 以下为新加表----------------------------------------
class Himageurl(models.Model):
    hid = models.OneToOneField('House', on_delete=models.CASCADE, db_column='hid', primary_key=True)
    hbigimageurl = models.CharField(max_length=255)
    himageorder = models.IntegerField(blank=True, null=True)
    isdownload = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'himageurl'
        unique_together = (('hid', 'hbigimageurl'),)






class HouseFacility(models.Model):
    hid = models.OneToOneField(House, on_delete=models.CASCADE, db_column='hid', primary_key=True)
    washer = models.IntegerField(blank=True, null=True)
    tv = models.IntegerField(db_column='TV', blank=True, null=True)  # Field name made lowercase.
    airconditioner = models.IntegerField(blank=True, null=True)
    freezer = models.IntegerField(blank=True, null=True)
    heating = models.IntegerField(blank=True, null=True)
    wifi = models.IntegerField(blank=True, null=True)
    lift = models.IntegerField(blank=True, null=True)
    gas = models.IntegerField(blank=True, null=True)
    water_heater = models.IntegerField(blank=True, null=True)
    parkinglot = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'house_facility'

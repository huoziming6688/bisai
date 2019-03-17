# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class City(models.Model):
    cid = models.CharField(primary_key=True, max_length=4)
    cityname = models.CharField(max_length=255, blank=True, null=True)
    provinceid = models.ForeignKey('Province', models.DO_NOTHING, db_column='provinceid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class District(models.Model):
    did = models.CharField(primary_key=True, max_length=6)
    districtname = models.CharField(max_length=255, blank=True, null=True)
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='cityid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Himageurl(models.Model):
    hid = models.ForeignKey('House', models.DO_NOTHING, db_column='hid', primary_key=True)
    hbigimageurl = models.CharField(max_length=255)
    himageorder = models.IntegerField(blank=True, null=True)
    isdownload = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'himageurl'
        unique_together = (('hid', 'hbigimageurl'),)


class House(models.Model):
    hid = models.CharField(primary_key=True, max_length=15)
    hyuanid = models.CharField(max_length=255, blank=True, null=True)
    htitle = models.TextField(blank=True, null=True)
    hsmallimageurl = models.CharField(max_length=255, blank=True, null=True)
    hurl = models.CharField(max_length=255, blank=True, null=True)
    subdistrictid = models.ForeignKey('Subdistrict', models.DO_NOTHING, db_column='subdistrictid', blank=True, null=True)
    himagedir = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house'


class HouseDetail(models.Model):
    hid = models.ForeignKey(House, models.DO_NOTHING, db_column='hid', primary_key=True)
    hprice = models.IntegerField(blank=True, null=True)
    hdirection = models.CharField(max_length=255, blank=True, null=True)
    htype = models.CharField(max_length=255, blank=True, null=True)
    harea = models.IntegerField(blank=True, null=True)
    hfloor = models.CharField(max_length=255, blank=True, null=True)
    hpubdate = models.CharField(max_length=255, blank=True, null=True)
    hcontact_info = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_detail'


class HouseFacility(models.Model):
    hid = models.ForeignKey(House, models.DO_NOTHING, db_column='hid', primary_key=True)
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
        managed = False
        db_table = 'house_facility'


class Province(models.Model):
    pid = models.CharField(primary_key=True, max_length=2)
    provincename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class Subdistrict(models.Model):
    sid = models.CharField(primary_key=True, max_length=11)
    yuanid = models.CharField(max_length=255)
    sname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    url = models.CharField(unique=True, max_length=255, blank=True, null=True)
    imageurl = models.CharField(max_length=255, blank=True, null=True)
    districtid = models.ForeignKey(District, models.DO_NOTHING, db_column='districtid', blank=True, null=True)
    issearch = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    imagedir = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subdistrict'


class SubdistrictLocation(models.Model):
    sid = models.ForeignKey(Subdistrict, models.DO_NOTHING, db_column='sid', primary_key=True)
    jingdu = models.CharField(max_length=255, blank=True, null=True)
    weidu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subdistrict location'


class SubdistrictDetail(models.Model):
    sid = models.ForeignKey(Subdistrict, models.DO_NOTHING, db_column='sid', primary_key=True)
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
        managed = False
        db_table = 'subdistrict_detail'


class UsersEmailverifyrecord(models.Model):
    code = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    send_type = models.CharField(max_length=10)
    send_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_emailverifyrecord'


class UsersUserprofile(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    nick_name = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=7)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users_userprofile'


class UsersUserprofileGroups(models.Model):
    userprofile = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_userprofile_groups'
        unique_together = (('userprofile', 'group'),)


class UsersUserprofileUserPermissions(models.Model):
    userprofile = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_userprofile_user_permissions'
        unique_together = (('userprofile', 'permission'),)


class XadminBookmark(models.Model):
    title = models.CharField(max_length=128)
    url_name = models.CharField(max_length=64)
    query = models.CharField(max_length=1000)
    is_share = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xadmin_bookmark'


class XadminLog(models.Model):
    action_time = models.DateTimeField()
    ip_addr = models.CharField(max_length=39, blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.CharField(max_length=32)
    message = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_log'


class XadminUsersettings(models.Model):
    key = models.CharField(max_length=256)
    value = models.TextField()
    user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_usersettings'


class XadminUserwidget(models.Model):
    page_id = models.CharField(max_length=256)
    widget_type = models.CharField(max_length=50)
    value = models.TextField()
    user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_userwidget'


class Xqimageurl(models.Model):
    sid = models.ForeignKey(Subdistrict, models.DO_NOTHING, db_column='sid', primary_key=True)
    bigimageurl = models.CharField(max_length=500)
    imageorder = models.IntegerField(blank=True, null=True)
    isdownload = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xqimageurl'
        unique_together = (('sid', 'bigimageurl'),)

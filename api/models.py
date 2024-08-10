# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.CharField(max_length=50, blank=True, null=True)
    road = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Categories(models.Model):
    categoryid = models.AutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categories'


class Member(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=128)
    user_email = models.CharField(unique=True, max_length=100)
    user_birth = models.DateField()
    user_avator = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'member'


class Spotimages(models.Model):
    imageid = models.AutoField(db_column='ImageId', primary_key=True)  # Field name made lowercase.
    spotid = models.IntegerField(db_column='SpotId', blank=True, null=True)  # Field name made lowercase.
    imagetitle = models.CharField(db_column='ImageTitle', max_length=300, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spotimages'


class Spots(models.Model):
    spotid = models.AutoField(db_column='SpotId', primary_key=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    spottitle = models.CharField(db_column='SpotTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spotdescription = models.TextField(db_column='SpotDescription', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trafficinfo = models.CharField(db_column='TrafficInfo', max_length=300, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=20, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=20, blank=True, null=True)  # Field name made lowercase.
    opentime = models.CharField(db_column='OpenTime', max_length=300, blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(db_column='ContactPhone', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spots'

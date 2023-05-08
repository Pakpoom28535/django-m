from django.db import models

# Create your models here.
class Employee(models.Model):
    CODE = models.CharField(max_length=30,primary_key=True)
    NAME_USER = models.CharField(max_length=30)
    SECTION = models.CharField(max_length=30)
    PASSWORD =  models.CharField(max_length=30)
    PERMITION = models.CharField(max_length=5,default='E')
    INSERTTIME = models.DateTimeField(auto_now_add=True)
    UPDATETIME = models.DateTimeField(auto_now=True)    
    def __str__(self):
    	return f"ID:{self.CODE}  Name: {self.NAME_USER} Permission: {self.PERMITION} "

class Product_ob(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_itemno = models.CharField(max_length=255,unique=True)
    product_description = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_qty = models.IntegerField()
    timein = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_description

class Location_rack_name(models.Model):
    rack_name_id= models.AutoField(primary_key=True)
    rack_name = models.CharField(max_length=255)

class Location_rack(models.Model):
    rack_id = models.AutoField(primary_key=True)
    rack_no = models.IntegerField()
    rack_name = models.ForeignKey(Location_rack_name, on_delete=models.CASCADE)

class Location_list(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255)
    Location_rack = models.ForeignKey(Location_rack, on_delete=models.CASCADE)
    Is_active = models.IntegerField(null=True,default=0)
class product_location(models.Model):
    product_location_id = models.AutoField(primary_key=True)
    Product_ob = models.ForeignKey(Product_ob,on_delete=models.CASCADE)
    Location_list = models.ForeignKey(Location_list,on_delete=models.CASCADE)
    timeupdate =  models.DateTimeField(auto_now=True)

class Custormer(models.Model):
    custormer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_contact = models.CharField(max_length=255)
    def __str__(self):
        return self.customer_name
class report_po(models.Model):
    po_id = models.AutoField(primary_key=True)
    po_name = models.CharField(max_length=255,null=True)
    Custormer =models.ForeignKey(Custormer,on_delete=models.CASCADE)
    timeupdate =  models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.po_id
class product_arrival(models.Model):
    arrival_id = models.AutoField(primary_key=True)
    Product_ob = models.ForeignKey(Product_ob,on_delete=models.CASCADE)
    location_arrival_no = models.CharField(max_length=255)
    location_arrival_name = models.CharField(max_length=255)
    qty  = models.IntegerField(null=True)
    total_price = models.FloatField(null=True)
    timeupdate =  models.DateTimeField(auto_now=True)
    arrival_report = models.IntegerField(null=True,default=0)
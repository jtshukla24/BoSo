from django.db import models


class Reg_Model(models.Model):
    t_id = models.IntegerField(default="")
    name = models.CharField(max_length=100, verbose_name='Name')
    email_id = models.CharField(max_length=100, verbose_name='Email ID', primary_key=True)
    password = models.CharField(max_length=10)
    mobile_no= models.IntegerField(default=10,null=True)
    address = models.CharField(max_length=100, verbose_name='Address', default="",null=True)
    confirm_password = models.CharField(max_length=10)


#
# class Student_Model(models.Model):
#     s_id = models.IntegerField(default="")
#     name = models.CharField(max_length=100, verbose_name='Name')
#     email_id = models.CharField(max_length=100, verbose_name='Email ID', primary_key=True)
#     password = models.CharField(max_length=10)
#     confirm_password = models.CharField(max_length=10)
#     section = models.IntegerField()
#     mobile = models.IntegerField(default=10)

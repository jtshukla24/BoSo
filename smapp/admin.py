from django.contrib import admin
from .models import *


class AdminReg(admin.ModelAdmin):
    list_display = ['name', 'email_id', 'password']


# class AdminTeacher(admin.ModelAdmin):
#     list_display = ['name', 'email_id', 'password']


admin.site.register(Reg_Model, AdminReg)
# admin.site.register(Student_Model, AdminStudent)

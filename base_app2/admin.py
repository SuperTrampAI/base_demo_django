from django.contrib import admin

# Register your models here.

from django.contrib import admin
from base_app2.models import Emp, Dept

# 把两个模型，加入到django自带的后台管理模型中

class DeptAdmin(admin.ModelAdmin):
    list_display = ("no", "name", "location")
    ordering = ("no",)


class EmpAdmin(admin.ModelAdmin):
    list_display = ("no", "name", "job", "mgr", "sal", "comm", "dept")
    search_fields = ("name", "job")


admin.site.register(Emp, EmpAdmin)
admin.site.register(Dept, DeptAdmin)

from django.contrib import admin
from features.models import ExportCSV,cuser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(ExportCSV)
admin.site.register(cuser,UserAdmin)
import imp
from django.contrib import admin
from .models import Taikhoan, Hocphan, Tudien
# Register your models here.
admin.site.register(Taikhoan)
admin.site.register(Hocphan)
admin.site.register(Tudien)
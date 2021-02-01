from django.contrib import admin
from .models import Choice, Question
# Register your models here.

#Đăng ký để trang admin hiển thị để thêm xoá sủa nhanh 
admin.site.register(Question)
admin.site.register(Choice)
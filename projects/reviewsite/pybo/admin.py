from django.contrib import admin
from .models import basic_info,detail_info
from embed_video.admin import AdminVideoMixin

# Register your models here.


admin.site.register(basic_info)
admin.site.register(detail_info)
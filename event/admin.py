from django.contrib import admin
from event.models import UserDetail,Place,Service,MicroBlog

admin.site.register(UserDetail)
admin.site.register(Place)
admin.site.register(Service)
admin.site.register(MicroBlog)

# Register your models here.

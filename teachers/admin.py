from django.contrib import admin
from .models import *

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('id','title',)

admin.site.site_header = "WALIMU MTANDAO"

admin.site.register(Mitaala, PageAdmin)
admin.site.register(Darasa, PageAdmin)
admin.site.register(Umahiri, PageAdmin)
admin.site.register(Umahsusi, PageAdmin)
admin.site.register(Shughuli, PageAdmin)
admin.site.register(Muhula, PageAdmin)

admin.site.register(Juma, PageAdmin)
admin.site.register(Siku, PageAdmin)
admin.site.register(Vipindi, PageAdmin)
#admin.site.register(MtaalaHead, PageAdmin)
#admin.site.register(MtaalaArticles, PageAdmin)

class MtaalaHeadAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','mtaala')
admin.site.register(MtaalaHead, MtaalaHeadAdmin) 

class MtaalaArticlesAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','headers')
admin.site.register(MtaalaArticles, MtaalaArticlesAdmin)  

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','email')
admin.site.register(User, UserAdmin)

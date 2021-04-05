from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class MyUserAdmin(BaseUserAdmin):
    list_display=('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields=('email','username') 
    readonly_fields=('date_joined','last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()
    ordering=('email',)

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','username','profile','phone','password1','password2'),
        }),
    )
admin.site.register(MyUser,MyUserAdmin)
admin.site.register(Room)
admin.site.register(Booking)
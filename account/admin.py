from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','firstname','lastname','username','last_login','date_join','is_admin','is_staff')
    search_fields = ('email','username','firstname','lastname')
    readonly_fields = ('date_join','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)
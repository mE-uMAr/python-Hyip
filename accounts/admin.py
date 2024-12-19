from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Customuser 


class CustomUserAdmin(UserAdmin):
    list_display = ('p_number', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('p_number', 'password')}),
        (_('Personal info'), {'fields': ('email', 'profile_img')}),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('p_number', 'email', 'password',  'is_staff', 'is_active'),
        }),
    )
    search_fields = ('p_number', 'email')
    ordering = ('p_number',)

admin.site.register(Customuser, CustomUserAdmin)

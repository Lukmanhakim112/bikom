from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'full_name', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('username', 'full_name', 'phone_number', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'full_name', 'phone_number', 'photo', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'phone_number')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)


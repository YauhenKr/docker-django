from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import NewUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additiona info',
            {
                'fields': (
                    'city',
                    'mobile_phone',
                )
            }
        )
    )


admin.site.register(NewUser, CustomUserAdmin)

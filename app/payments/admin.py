"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from payments import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['name']
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     (_('Personal Info'), {'fields': ('name',)}),
    #     (
    #         _('Permissions'),
    #         {
    #             'fields': (
    #                 'is_active',
    #                 'is_staff',
    #                 'is_superuser',
    #             )
    #         }
    #     ),
    #     (_('Important dates'), {'fields': ('last_login',)}),
    # )
    readonly_fields = ['created_at', 'updated_at']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
              'name',
              'is_active',
              'description',
              'created_at',
              'updated_at'
            ),
        }),
    )


admin.site.register(models.PaymentMethod)
admin.site.register(models.PaymentMethodUser)
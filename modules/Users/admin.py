from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA

from  .models import User


class UserAdmin(UA):

    fieldsets = (
        ('Account', {
            'fields': ('email', 'password', 'is_active', 'is_staff')
        }), ('Personal Fields', {
            'fields': ('name', 'last_name','cel_phone','gender','library')

        })

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    def username(self, instance):
        return instance.email

    def user_first_name (self,instance):
        return instance.name

    def user_last_name (self,instance):
        return instance.last_name

    list_display = ('email', 'user_first_name', 'user_last_name','is_active')
    ordering = ('email',)

admin.site.register(User, UserAdmin)
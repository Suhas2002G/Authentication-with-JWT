from django.contrib import admin
from account.models import User 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    list_display = ["id","email","name","mobile", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","mobile"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","mobile", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["id","email"]
    filter_horizontal = []


# Now register the new UserModelAdmmin...
admin.site.register(User, UserModelAdmin)





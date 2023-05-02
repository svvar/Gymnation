from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

admin.site.unregister(Group)

class AdminUser(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    list_display = ['email', 'is_superuser']
    list_filter = ['is_superuser']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'club', 'plan', 'trainer', 'photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'club', 'plan', 'trainer', 'photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, AdminUser)
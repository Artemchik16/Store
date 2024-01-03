from django.contrib import admin
from django.contrib.auth import get_user_model

from carts.admin import CartTabularAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "full_name")
    list_display_links = ('username', 'id')
    search_fields = ('username', )
    inlines = (CartTabularAdmin, )

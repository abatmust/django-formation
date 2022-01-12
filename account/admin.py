from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "email", "state", "created")
    list_filter = ("state",)
    list_display_links = ('username',)
    search_fields = ("name", "username", "email",)
    list_per_page = 4


admin.site.register(Profile, ProfileAdmin)

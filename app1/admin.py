'''from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('user__username', 'mobile')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

'''
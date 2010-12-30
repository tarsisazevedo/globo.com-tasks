from django.contrib import admin
from favoritos.models import Favorito, Usuario
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User

class UserProfileInline(admin.TabularInline):
    model = Usuario
        
class UserAdmin(DjangoUserAdmin):
    inlines = (UserProfileInline,)
                
admin.site.unregister(User)               
admin.site.register(User, UserAdmin)
admin.site.register(Favorito)

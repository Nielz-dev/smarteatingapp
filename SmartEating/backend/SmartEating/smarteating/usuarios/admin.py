from django.contrib import admin
from .models import UserAccount

# Register your models here.

# UD8.1D Creo la clase MyUserAdmin para poder gestionar el panel de administrador de usuarios.
class UserAccountAdmin (admin.ModelAdmin):
    list_display = ('email','first_name','last_name')
    list_display_links = ('email','first_name','last_name')
    search_fields = ['email','first_name','last_name']
    readonly_fields = ('id',)
    

admin.site.register(UserAccount, UserAccountAdmin)

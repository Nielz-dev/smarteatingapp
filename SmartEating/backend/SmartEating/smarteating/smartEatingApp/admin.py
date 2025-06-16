from django.contrib import admin
from .models import *

class PlatoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nombre', 'fecha', 'foto_perfil', 'mostrar_ingredientes']
    readonly_fields = ('id',)

    def mostrar_ingredientes(self, obj):
        return ", ".join([ingrediente.nombre for ingrediente in obj.ingredientes.all()])

    mostrar_ingredientes.short_description = 'Ingredientes'

class IngredienteAdmin (admin.ModelAdmin):
    list_display = ('nombre','cantidad','tipo_peso')
    list_display_links = ('nombre','cantidad','tipo_peso')
    search_fields = ['nombre','cantidad','tipo_peso']
    readonly_fields = ('id',)    
    

admin.site.register(Plato, PlatoAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)

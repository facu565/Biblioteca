from django.contrib import admin
from .models import *


# Register your models here.

class PrestamoInLine(admin.TabularInline): 
    model = Prestamo

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('fechaSalida','fechaRegreso','persona', 'material',)
    list_filter = ('persona','material','fechaSalida','fechaRegreso',)
    
class AlumnoAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    list_display = ('matricula', 'apellido',)
    search_fields = ['nombre', 'apellido', 'correo','matricula']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido',)
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono',)
        }),
        ('Alumno', {
            'fields': ('matricula',)
        }),
        ('Bibloteca', {
            'fields': ('numLibros','adeudo',)
        }),
    )

class MaterialAdmin(admin.ModelAdmin):
    pass

class ProfesorAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    search_fields = ['nombre', 'apellido', 'correo', 'telefono', 'numEmpleado']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido',)
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono',)
        }),
        ('Empleado', {
            'fields': ('numEmpleado',)
        }),
        ('Bibloteca', {
            'fields': ('numLibros','adeudo',)
        }),
    )


class LibroAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    list_display = ('titulo', 'autor',)
    search_fields = ['titulo', 'autor',]
    list_filter = ('autor','year',)
    fieldsets = (
        ("Material", {
            'fields': ('codigo', 'autor','titulo','year',)
        }),
        ('Estado', {
            'fields': ('status',)
        }),
    )

class RevistaAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    list_display = ('titulo', 'autor',)
    search_fields = ['titulo', 'autor', ]
    list_filter = ('autor', 'year',)
    fieldsets = (
        ("Material", {
            'fields': ('codigo', 'autor', 'titulo', 'year')
        }),
        ('Estado', {
            'fields': ('status',)
        }),
    )

admin.site.register(Material,MaterialAdmin)
admin.site.register(Prestamo,PrestamoAdmin)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Revista,RevistaAdmin)
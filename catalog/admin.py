from django.contrib import admin
from .models import Patient, Case, Visit
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.html import format_html
# admin.site.register(Patient)
#admin.site.register(Case)
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    readonly_fields =('id',)
    list_display =  ('date', 'id_c',)
    
class VisitInline(admin.TabularInline):
    model = Visit
    extra = 0
    readonly_fields =('id',)
    list_display = ('id_c', 'date',)
    list_display_link = ('id',)
    can_delete = False
    show_change_link = True

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    readonly_fields =('id',)
    list_display =  ('date', 'id')
    date_hierarchy = 'date'
    inlines = [VisitInline]
    
class CaseInline(admin.TabularInline):
    model = Case
    extra = 0
    readonly_fields =('id',)
    list_display = ('id', 'date','reason','result')
    list_display_link = ('id',)
    can_delete = False
    show_change_link = True

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    ordering = ('last_name',)
    search_fields = ('last_name','oms',)
    fieldsets = (
        ('Данные пациента', {
            'fields': ('id',('first_name','last_name','patronym'),'sex','date')
        }),
        ('Документы и льготы', {
            'fields': (('smo', 'oms'), 'disability',)

        },
    ))
    list_filter = ('last_name','disability','date',)
    list_display = ('id', 'first_name', 'last_name', 'date', 'oms')
    inlines = [CaseInline]

@staff_member_required
def staff_view(redirect_field_name='patient',login_url='admin:leo'):
    ...
# Register the Admin classes for BookInstance using the decorator







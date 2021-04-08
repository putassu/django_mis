from django.contrib import admin
from .models import Patient, Case, Visit
# admin.site.register(Patient)
admin.site.register(Case)
class CaseInline(admin.TabularInline):
    model = Case
    extra = 0
admin.site.register(Visit)
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

# Register the Admin classes for BookInstance using the decorator





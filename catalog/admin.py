from django.contrib import admin
from catalog.models import Patient, Visit, Diagnosis, Case, Service, Schedule
from django.utils.html import format_html
# admin.site.register(Patient)
#admin.site.register(Case)
from catalog.forms import Form, Form2

# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ('date','id_10_00','id_10_20',)
admin.site.register(Schedule)

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('services',)


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0
    readonly_fields = ('id',)
    list_display = ('id_v', 'services',)
    list_display_link = ('id',)
    can_delete = False
    show_change_link = True
admin.site.register(Service, ServiceAdmin)


class VisitAdmin(admin.ModelAdmin):
    # readonly_fields =('id',)
    exclude = ('id',)
    list_display = ('date', 'help_type','services')
    form = Form2


class VisitInline(admin.TabularInline):
    model = Visit
    extra = 0
    # readonly_fields =('id',)
    list_display = ('date', 'help_type',)
    # list_display_link = ('id',)
    exclude = ('id',)
    can_delete = False
    show_change_link = True


admin.site.register(Visit, VisitAdmin)

# @admin.register(Case)



class CaseAdmin(admin.ModelAdmin):
    # readonly_fields =('id',)
    list_display = ('date', 'character', 'reason', 'result', 'diagnosis','doctor')
    date_hierarchy = 'date'
    exclude = ('id',)
    inlines = [VisitInline]
    # admin.ModelAdmin.filter_horizontal = ('diagnosis',  )
    form = Form
#
# class CollectionAdmin(admin.ModelAdmin):
#     filter_horizontal = ('author',)

admin.site.register(Case, CaseAdmin)

class CaseInline(admin.TabularInline):
    model = Case
    extra = 0
    readonly_fields_ = [field.name for field in Case._meta.fields]
    readonly_fields = readonly_fields_[5:]
    list_display = ('date', 'reason', 'result')
    list_display_link = ('date',)
    exclude = ('id',)
    can_delete = False
    show_change_link = True

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    ordering = ('last_name',)
    search_fields = ('last_name','oms',)
    fieldsets = (
        ('Данные пациента', {
            'fields': (('first_name','last_name','patronym'),'sex','date')
        }),
        ('Документы и льготы', {
            'fields': (('smo', 'oms'), 'disability',)

        },
    ))
    list_filter = ('last_name','disability','date',)
    list_display = ('id', 'first_name', 'last_name', 'date', 'oms')
    inlines = [CaseInline]


admin.site.register(Diagnosis)
# Register the Admin classes for BookInstance using the decorator




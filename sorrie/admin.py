from mptt.admin import DraggableMPTTAdmin
from django.contrib import admin
import csv
from sorrie.models import Dentist, Patient, Post, Category
from django.http import HttpResponse


admin.site.register(Dentist)
admin.site.register(Patient)


admin.site.register(Post)
admin.site.register(Category , DraggableMPTTAdmin)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


# @admin.register(Dentist)
# class DentistAdmin(admin.ModelAdmin, ExportCsvMixin):
#
#     readonly_fields = [..., "dentist_photo"]
#
#     def dentist_photo(self, obj):
#         return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
#             url = obj.dentist.url,
#             width=obj.dentist.width,
#             height=obj.dentist.height,
#             )
#     )
#

#class DentistAdmin(admin.ModelAdmin):
 #   fields = ['pub_date', 'dentist_name','dentist_address','dentist_number','dentist_neigh','dentist_city', 'dentist_mobile','dentist_cro']


#admin.site.register(Dentist, DentistAdmin)



# Register your models here.

#
# dentist_name = models.CharField(max_length=60)
#     dentist_address = models.CharField(max_length=150)
#     dentist_city = models.CharField(max_length=50)
#     dentist_neigh = models.CharField(max_length=50)
#     dentist_number = models.BigIntegerField(max_length=6)
#     dentist_mobile = models.BigIntegerField(max_length=14)
#     dentist_cro = models.BigIntegerField(max_length=6)
#     pub_date = models.DateT
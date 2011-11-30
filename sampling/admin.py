# Enable use of Admin Interface

from sampling.models import *
from company.models import *
from gps.models import *
#from django.contrib import admin
from django.contrib.gis import admin

class StatusInline(admin.StackedInline):
    model = Status
    fieldsets = [
        (None, {'fields': ['report']}),
        ('Pre-Import', {'fields': ['data_validated', 'edd_prep_pre_validation',
                                   'edd_prep_post_validation']}),
        ('Screening Criteria', {'fields': ['screening_criteria_chosen', 'reg_limits_added','reg_limits_updated', 'wiki_reg_limit_groups_updated','wiki_reg_limit_dates_updated']}),
        ('Post-Import', {'fields': ['edd_imported', 'sample_group_created', 'draft_table_produced', 'draft_qa_qc','final_formatting']})
]

# Create custom fieldset for status
class StatusAdmin(admin.ModelAdmin):
    list_display = ('report',)
    fieldsets = [
        (None, {'fields': ['report']}),
        ('Pre-Import', {'fields': ['data_validated', 'edd_prep_pre_validation',
                                   'edd_prep_post_validation']}),
        ('Screening Criteria', {'fields': ['screening_criteria_chosen', 'reg_limits_added','reg_limits_updated', 'wiki_reg_limit_groups_updated','wiki_reg_limit_dates_updated']}),
        ('Post-Import', {'fields': ['edd_imported', 'sample_group_created', 'draft_table_produced', 'draft_qa_qc','final_formatting']})
    ]

# Display detailed project information
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'client')

# Augment report overview with project and date submitted
# and report detail with info from status model
class ReportAdmin(admin.ModelAdmin):
    inlines=[StatusInline]
    list_display = ('name', 'project', 'date_submitted')


class SDGAdmin(admin.ModelAdmin):
    list_display = ('name', 'lab', 'report')

# Add each model to the admin

# Company App
admin.site.register(Client)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Boundary, admin.OSMGeoAdmin)

# Sampling App
admin.site.register(Lab)
admin.site.register(SDG, SDGAdmin)
admin.site.register(Status, StatusAdmin)

# GPS App
admin.site.register(Site_Poly, admin.OSMGeoAdmin)
admin.site.register(Site_Point, admin.OSMGeoAdmin)
admin.site.register(Site_Line, admin.OSMGeoAdmin)
admin.site.register(GPS_Poly, admin.OSMGeoAdmin)
admin.site.register(GPS_Point, admin.OSMGeoAdmin)
admin.site.register(GPS_Line, admin.OSMGeoAdmin)
admin.site.register(Feature_Type)
admin.site.register(GPS_Metadata)

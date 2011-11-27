#from django.db import models
from django.contrib.gis.db import models

# A GIS Model containing WA/AK Reservation Boundaries
class Boundary(models.Model):
    name = models.CharField('Name', max_length=100)
    name_formal = models.CharField('Formal Name', max_length=100)

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Tribal Boundary'
        verbose_name_plural = 'Tribal Boundaries'

# Tabular models
class Client(models.Model):
    name = models.CharField('Client Name', max_length=100)
    boundary = models.ForeignKey(Boundary, null=True, blank=True)
    # Function to return Alias (useful in admin)
    def __unicode__(self):
        return self.name
   
    # Controls default ordering and appearance of model name
    # in admin manager.
    class Meta:
        ordering = ['name']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

class Project(models.Model):
    name = models.CharField('Project Name', max_length=100)
    number = models.CharField('Project Number', max_length=10)
    client = models.ForeignKey(Client)

    # Function to return Alias (useful in admin)
    def __unicode__(self):
        return self.number

    class Meta:
        ordering = ['number']

class Report(models.Model):
    name = models.CharField('Report Name', max_length = 100)
    project = models.ForeignKey(Project)
    date_submitted = models.DateField('Date Submitted', null=True, blank=True) 

    # Function to return Alias (useful in admin)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Lab(models.Model):
    name = models.CharField('Analytical Lab', max_length=75)

    # Function to return Alias (useful in admin)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class SDG(models.Model):    
    name = models.CharField('SDG Name', max_length = 25)
    lab = models.ForeignKey(Lab)
    report = models.ForeignKey(Report)
    recieved_edd = models.BooleanField('Recieved EDD')
    recieved_hardcopy = models.BooleanField('Recieved Hardcopy')

    # Function to return Alias (useful in admin)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'SDG'
        verbose_name_plural = 'SDGs'
        ordering = ['name']

class Status(models.Model):
    report = models.OneToOneField(Report)
    data_validated = models.BooleanField('Data Validated')
    edd_prep_pre_validation = models.BooleanField('Non-Validated EDD Prepared for Import')
    edd_prep_post_validation = models.BooleanField('Validated EDD Prepared for Import')
    screening_criteria_chosen = models.BooleanField('Screening Criteria Chosen')
    reg_limits_added = models.BooleanField('Regulatory Limits Added to EnviroData')
    reg_limits_updated = models.BooleanField('Existing Regulatory Limits Updated')
    wiki_reg_limit_groups_updated = models.BooleanField('Wiki Updated With Reg Limit Groups')
    wiki_reg_limit_dates_updated = models.BooleanField('Wiki Updated With Reg Limit Dates')
    edd_imported = models.BooleanField('EDD Imported Into EnviroData')
    sample_group_created = models.BooleanField('Sample Group Created in EnviroData')
    draft_table_produced = models.BooleanField('Draft Table Produced')
    draft_qa_qc = models.BooleanField('Draft Tables QA/QC Against Hardcopy')
    final_formatting = models.BooleanField('Tables Undergone Final Formatting')

    # Function to return Alias (useful in admin)
   # def __unicode__(self):
   #     return self.report
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

# A GIS Model containing WA/AK Reservation Boundaries
"""
class Boundary(models.Model):
    name = models.CharField('Name', max_length=100)
    name_formal = models.CharField('Formal Name', max_length=100)
    client = models.ForeignKey(Client)

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Tribal Boundary'
        verbose_name_plural = 'Tribal Boundaries'
"""

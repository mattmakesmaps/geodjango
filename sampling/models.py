from django.contrib.gis.db import models
from company.models import Boundary, Client, Project, Report

class Lab(models.Model):
    """Analytical labs."""

    name = models.CharField('Analytical Lab', max_length=75)

    # Function to return Alias (useful in admin)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class SDG(models.Model):
    """The sample digestion group."""    

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
    """The status of a report."""

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

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

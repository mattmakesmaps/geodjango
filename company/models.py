from django.contrib.gis.db import models

# A GIS Model containing WA/AK Reservation Boundaries
class Boundary(models.Model):
    name = models.CharField('Name', max_length=100)
    name_formal = models.CharField('Formal Name', max_length=100)

    geom = models.MultiPolygonField()
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



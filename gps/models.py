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

# GPS Models
class GPS_Point(models.Model):
    pass

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Point'
        verbose_name_plural = 'GPS Points'

class GPS_Line(models.Model):
    pass

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Line'
        verbose_name_plural = 'GPS Lines'

class GPS_Poly(models.Model):
    pass

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Polygon'
        verbose_name_plural = 'GPS Polygons'

# Supporting Site Features
class Site_Point(models.Model):
    name = models.CharField('Name', max_length=100)
    feature_type = models.ForeignKey(Feature_Type)
    projects = models.ManyToManyField(Project)

    geom = models.MultiPointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Site Point'
        verbose_name_plural = 'Sites Points'

class Site_Line(models.Model):
    name = models.CharField('Name', max_length=100)
    feature_type = models.ForeignKey(Feature_Type)
    projects = models.ManyToManyField(Project)

    geom = models.MultiLineStringField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Site Lines'
        verbose_name_plural = 'Site Lines'

class Site_Poly(models.Model):
    name = models.CharField('Name', max_length=100)
    feature_type = models.ForeignKey(Feature_Type)
    projects = models.ManyToManyField(Project)

    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Site Polygon'
        verbose_name_plural = 'Site Polygons'

# Tabular models
class Feature_Type(models.Model):
    name = models.CharField('Name', max_length = 100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Feature Type'
        verbose_name_plural = 'Feature Types'

class gps_metadata(models.Model):
    name = models.CharField('File Name', max_length = 100)
    # Think about alternative field types
    pathway = models.CharField('File Path', max_length = 500)
    report = models.ForeignKey(Report)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Metadata'
        verbose_name_plural = 'GPS Metadata'

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

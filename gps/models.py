from django.contrib.gis.db import models
from company.models import Boundary, Client, Project, Report

# Supplementary Info for GPS/Site Features
class Feature_Type(models.Model):
    name = models.CharField('Name', max_length = 100)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = 'Feature Type'
        verbose_name_plural = 'Feature Types'

"""
def default_type():
    try:
        g = Feature_Type.objects.get(name='undefined')
        return g
    except:
        g = Feature_Type(name='undefined')
        g.save()
        return g
"""
class GPS_Metadata(models.Model):
    name = models.CharField('File Name', max_length = 100)
    # Think about alternative field types
    pathway = models.CharField('File Path', max_length = 500)
    report = models.ForeignKey(Report, blank=True)

    def __unicode__(self):
        return self.name
  
    class Meta:
        verbose_name = 'GPS Metadata'
        verbose_name_plural = 'GPS Metadata'
""" 
def default_gps_metadata():
    try:
        g = GPS_Metadata.objects.get(name='undefined')
        return g
    except:
        g = GPS_Metadata(name='undefined',pathway='undefined')
        g.save()
        return g
"""

# GPS Models
class GPS_Point(models.Model):
    name = models.CharField('Name', max_length=50)
    max_pdop = models.DecimalField('Max_PDOP', max_digits=5, decimal_places=1, blank=True)
    gps_date = models.DateField('GPS_Date')
    gps_time = models.CharField('GPS_Time', max_length=50)
    feat_name = models.CharField('Feat_Name', max_length=50)
    feature_type = models.ForeignKey(Feature_Type, default=Feature_Type.objects.filter(name='undefined'))
    gps_metadata = models.ForeignKey(GPS_Metadata, default=GPS_Metadata.objects.filter(name='undefined'))

    geom = models.MultiPointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Point'
        verbose_name_plural = 'GPS Points'

class GPS_Line(models.Model):
    name = models.CharField('Name', max_length=50)
    max_pdop = models.DecimalField('Max_PDOP', max_digits=5, decimal_places=1, blank=True)
    gps_date = models.DateField('GPS_Date')
    gps_time = models.CharField('GPS_Time', max_length=50)
    feat_name = models.CharField('Feat_Name', max_length=50)
    feature_type = models.ForeignKey(Feature_Type, default='Uncategorized')
    gps_metadata = models.ForeignKey(GPS_Metadata, default='Uncategorized')

    geom = models.MultiLineStringField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Line'
        verbose_name_plural = 'GPS Lines'

class GPS_Poly(models.Model):
    name = models.CharField('Name', max_length=50)
    max_pdop = models.DecimalField('Max_PDOP', max_digits=5, decimal_places=1, blank=True)
    gps_date = models.DateField('GPS_Date')
    gps_time = models.CharField('GPS_Time', max_length=50, default='Uncategorized')
    feat_name = models.CharField('Feat_Name', max_length=50, default='Uncategorized')
    feature_type = models.ForeignKey(Feature_Type)
    gps_metadata = models.ForeignKey(GPS_Metadata)

    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Polygon'
        verbose_name_plural = 'GPS Polygons'

# Supporting Site Features
class Site_Point(models.Model):
    name = models.CharField('Name', max_length=100)
    feature_type = models.ForeignKey(Feature_Type, default='Uncategorized')
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
    feature_type = models.ForeignKey(Feature_Type, default='Uncategorized')
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
    feature_type = models.ForeignKey(Feature_Type, default='Uncategorized')
    projects = models.ManyToManyField(Project)

    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Site Polygon'
        verbose_name_plural = 'Site Polygons'

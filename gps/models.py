from django.contrib.gis.db import models
from company.models import Boundary, Client, Project, Report

class Feature_Type(models.Model):
    """Supplementary info for GPS and Site Features."""

    name = models.CharField('Name', max_length = 100)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = 'Feature Type'
        verbose_name_plural = 'Feature Types'

class GPS_Metadata(models.Model):
    """An individual GPS data batch."""

    name = models.CharField('File Name', max_length = 100)
    # Think about alternative field types
    pathway = models.CharField('File Path', max_length = 500)
    report = models.ForeignKey(Report, blank=True, null=True)

    def __unicode__(self):
        return self.name
  
    class Meta:
        verbose_name = 'GPS Metadata'
        verbose_name_plural = 'GPS Metadata'

# GPS Models
class GPS_Point(models.Model):
    """GPS Point features."""

    name = models.CharField('Name', max_length=50)
    max_pdop = models.DecimalField('Max_PDOP', max_digits=5, decimal_places=1, blank=True, null=True)
    gps_date = models.DateField('GPS_Date', blank=True, null=True)
    gps_time = models.CharField('GPS_Time', max_length=50, blank=True, null=True)
    gps_week = models.IntegerField('GPS_Week', max_length=10, blank=True, null=True)
    gps_second = models.IntegerField('GPS_Second', max_length=10, blank=True, null=True)
    feat_name = models.CharField('Feat_Name', max_length=50, blank=True, null=True)
    feature_type = models.ForeignKey(Feature_Type, default=Feature_Type.objects.filter(name='undefined'), blank=True, null=True)
    gps_metadata = models.ForeignKey(GPS_Metadata, default=1, blank=True, null=True)

    geom = models.MultiPointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Point'
        verbose_name_plural = 'GPS Points'

class GPS_Line(models.Model):
    """GPS Line features."""

    name = models.CharField('Name', max_length=50)
    max_pdop = models.DecimalField('Max_PDOP', max_digits=5, decimal_places=1, blank=True, null=True)
    gps_date = models.DateField('GPS_Date', blank=True, null=True)
    gps_time = models.CharField('GPS_Time', max_length=50, blank=True, null=True)
    gps_week = models.IntegerField('GPS_Week', max_length=10, blank=True, null=True)
    gps_second = models.IntegerField('GPS_Second', max_length=10, blank=True, null=True)
    feat_name = models.CharField('Feat_Name', max_length=50, blank=True, null=True)
    feature_type = models.ForeignKey(Feature_Type, default=Feature_Type.objects.filter(name='undefined'), blank=True, null=True)
    gps_metadata = models.ForeignKey(GPS_Metadata, default=GPS_Metadata.objects.filter(name='undefined'), blank=True, null=True)

    geom = models.MultiLineStringField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Line'
        verbose_name_plural = 'GPS Lines'

class GPS_Poly(models.Model):
    """GPS polygon features."""

    name = models.CharField('Name', max_length=50)
    max_pdop = models.DecimalField('Max_PDOP', max_digits=5, decimal_places=1, blank=True, null=True)
    gps_date = models.DateField('GPS_Date', blank=True, null=True)
    gps_time = models.CharField('GPS_Time', max_length=50, blank=True, null=True)
    gps_week = models.IntegerField('GPS_Week', max_length=10, blank=True, null=True)
    gps_second = models.IntegerField('GPS_Second', max_length=10, blank=True, null=True)
    feat_name = models.CharField('Feat_Name', max_length=50, blank=True, null=True)
    feature_type = models.ForeignKey(Feature_Type, default=Feature_Type.objects.filter(name='undefined'), blank=True, null=True)
    gps_metadata = models.ForeignKey(GPS_Metadata, default=GPS_Metadata.objects.filter(name='undefined'), blank=True, null=True)

    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'GPS Polygon'
        verbose_name_plural = 'GPS Polygons'

# Supporting Site Features
class Site_Point(models.Model):
    """Site-specific point features."""

    name = models.CharField('Name', max_length=100)
    feature_type = models.ForeignKey(Feature_Type, default='undefined', blank=True, null=True)
    projects = models.ManyToManyField(Project)

    geom = models.MultiPointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Site Point'
        verbose_name_plural = 'Sites Points'

class Site_Line(models.Model):
    """Site-specific line features."""

    name = models.CharField('Name', max_length=100)
    feature_type = models.ForeignKey(Feature_Type, default='undefined', blank=True)
    projects = models.ManyToManyField(Project)

    geom = models.MultiLineStringField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Site Lines'
        verbose_name_plural = 'Site Lines'

class Site_Poly(models.Model):
    """Site-specific polygon features."""

    name = models.CharField('Name', max_length=100)
    feature_type = models.ForeignKey(Feature_Type, default='Uncategorized', blank=True)
    projects = models.ManyToManyField(Project)

    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Site Polygon'
        verbose_name_plural = 'Site Polygons'

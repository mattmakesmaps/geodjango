from vectorformats.Formats import Django, GeoJSON
from decimal import Decimal
from datetime import date
import django.db.models.base

# Utility Functions
def djangoToGeoJSON(request, filter_object, properties_list=None, geom_col="geom"):
    """Convert a GeoDjango QuerySet to a GeoJSON Object"""
    
    #Workaround for mutable default value
    if properties_list==None:
        properties_list = []
        #Return dictionary of key value pairs
        filter_dict = filter_object[0].__dict__
        #Remove bunk fields
        for d in filter_dict:
            if isinstance(filter_dict[d], django.db.models.base.ModelState):
                pass
            # Convert decimal to float
            elif isinstance(filter_dict[d], Decimal):
                for obj in filter_object:
                    setattr(obj, d, float(obj.__dict__[d]))
                properties_list.append(d)    
            # Convert date to string
            elif isinstance(filter_dict[d], date):
                for obj in filter_object:
                    setattr(obj, d, str(obj.__dict__[d]))
                properties_list.append(d)
            else:
                properties_list.append(d)

        properties_list.remove(geom_col)

    queryset = filter_object
    djf = Django.Django(geodjango=geom_col, properties=properties_list)
    decode_djf = djf.decode(queryset)
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(decode_djf)
    return s


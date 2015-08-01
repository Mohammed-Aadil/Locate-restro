from rest_framework_gis.serializers import GeoFeatureModelSerializer
from main.models import restro
from django.contrib.auth.models import User

class DataSerializer(GeoFeatureModelSerializer):
    class Meta:
        model=restro
        geo_field="mpoint"
        fields=('id','name','lat','lon','user')
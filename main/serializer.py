from rest_framework import serializers
from main.models import restro
from django.contrib.auth.models import User

class DataSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source="user.username")
    class Meta:
        model=restro
        fields=('id','name','mpoint','lat','lon','user')
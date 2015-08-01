from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_203_NON_AUTHORITATIVE_INFORMATION

from main.models import restro
from main.serializer import DataSerializer


# Create your views here.
@api_view(['GET','POST'])
def locate(request):
    if(request.method=="GET"):
        r=restro.objects.all()
        s=DataSerializer(r, many=True)
        return Response(s.data)
    elif(request.method=="POST"):
        return Response(status=status.HTTP_302_FOUND)

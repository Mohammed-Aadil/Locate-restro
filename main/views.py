from django.contrib.auth.models import User
from django.contrib.gis.geos.point import Point
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import restro
from main.serializer import DataSerializer


# Create your views here.
def index(request):
    return render(request,'main/auth.html')

@api_view(['GET','POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def locate(request):
    if(request.method=="POST" and User.objects.filter(username=request.user)):
        lat=float(request.POST.get('latitude'))
        lon=float(request.POST.get('longitude'))
        point=Point(lon,lat)
        restrodata=restro.objects.filter(mpoint__distance_lte=(point,5000))
        serializer=DataSerializer(restrodata, many=True)
        return Response(serializer.data)
    
    
@csrf_exempt
def Auth_token(request):
    if(request.method=="POST"):
        try:
            usr=User.objects.get(username=request.POST['username'])
            if(usr.check_password(request.POST['password'])==True):
                t=Token.objects.get_or_create(user=usr)
                print(t)
                return HttpResponse(t)
            return HttpResponse("Unauthorized User",status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return HttpResponse("Unauthorized User", status=status.HTTP_401_UNAUTHORIZED)
    return HttpResponse("400 - Bad Request", status=status.HTTP_400_BAD_REQUEST)

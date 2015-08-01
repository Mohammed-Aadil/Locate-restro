from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_203_NON_AUTHORITATIVE_INFORMATION

from main.models import restro
from main.serializer import DataSerializer
from rest_framework.authtoken.models import Token
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request,'main/auth.html')

@api_view(['GET','POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def locate(request):
    if(request.method=="GET" and User.objects.filter(username=request.user)):
        r=restro.objects.all()
        s=DataSerializer(r, many=True)
        return Response(s.data)
    
    
@csrf_exempt
def Auth_token(request):
    if(request.method=="POST"):
        try:
            usr=User.objects.get(username=request.POST['username'])
            if(usr.check_password(request.POST['password'])==True):
                t=Token.objects.get_or_create(user=usr)
                print(t)
                return HttpResponse(t)
            
            return HttpResponse("Unauthorized User")
        except Exception:
            return HttpResponse("Unauthorized User")
    return HttpResponse("400 - Bad Request")
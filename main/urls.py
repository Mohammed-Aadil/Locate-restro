from django.conf.urls import url,patterns
from main import views

urlpatterns=patterns('',
                     url(r'^login/$', views.index,name="index"),
                     url(r'^locate/$', views.locate,name="locate"),
                     url(r'^get-auth-token/$', views.Auth_token, name="token"),
                     )
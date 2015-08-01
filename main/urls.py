from django.conf.urls import url,patterns
from main import views

urlpatterns=patterns('',
                     url(r'^locate/$', views.locate,name="locate"),
                     )
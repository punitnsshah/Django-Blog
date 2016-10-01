from django.conf.urls import url
from src import views

urlpatterns=[
    url(r'', views.index, name="index")
]
from rest_framework.urls import urlpatterns
from django.urls import  path
from . import  views
urlpatterns =[
        path('creator/',views.AdminPanel.as_view(),name="creator")

]
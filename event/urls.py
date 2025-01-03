
from django.urls import  path
from . import views
from . import views

urlpatterns =[
    path("create/",views.CreateEvent.as_view(),name ="event"),
    path("list/",views.ListEvent.as_view(),name="all"),
    path("<str:id_event>/",views.Event.as_view(),name="get event")
]


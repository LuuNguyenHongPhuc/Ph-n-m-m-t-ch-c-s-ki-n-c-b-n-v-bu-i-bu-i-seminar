
from django.urls import  path
from . import views


urlpatterns =[
    path("create/",views.CreateEvent.as_view(),name ="create_event"),
    path("list/",views.ListEvent.as_view(),name="list_event"),
    path("gevent/<str:id_event>/",views.Event.as_view(),name="event"),
    path("eventcart/",views.User_MyEvent.as_view(),name="eventcart"),
    path("edit/<str:id_event>/",views.EditEvent.as_view(),name="edit_event")
]


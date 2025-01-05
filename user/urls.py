from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', views.dangnhap, name='login'),
  
    path('register/', views.dangky, name='register'),

    path('info/',views.UserInfo.as_view(),name="info"),
    path('logout/',views.logout_view,name="logout")
]


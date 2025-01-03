from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.dangnhap, name='login'),
    # Đường dẫn đến view đăng nhập
    path('register/', views.dangky, name='register'),

    path('home/',views.home,name="home"),
    path('logout/',views.logout_view,name="logout")
]

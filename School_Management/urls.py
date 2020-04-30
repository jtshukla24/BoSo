"""School_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from smapp import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home,name='index'),
    path('index_page/', views.home),
    path('tsignup/',views.user_signup_view),
    path('profile/',views.profile_view,name='profile'),
    path('login/',views.login_view),
    path('about/',views.about_view),
    path('ad_fee/',views.ad_fees),
    path('fee/',views.fee_view),
    path('withdraw/',views.withdraw_view),
    path('facilities/',views.facilities_view),
    path('fac_read_more/',views.fac_read_more,name='fac_read'),
    path('acti_read_more/',views.acti_read_more,name='acti_read'),
    path('acad_read_more/',views.acad_read_more,name='acad_read'),
    path('board_read_more/',views.board_read_more,name='board_read'),
    path('games_read_more/',views.games_read_more,name='game_read'),
    path('new_read_more/',views.new_read_more,name='new_read'),
    path('parents/',views.parents),
    path('teachers/',views.teachers)


    # path('tlogin/',views.user_login_view),
    # path('ssignup/',views.student_signup_view),


]

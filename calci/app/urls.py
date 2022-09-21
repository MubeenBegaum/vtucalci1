from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home ,name='home'),

   path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
     path('index/',views.index,name='index'),
   # path('profile/',views.profile, name='profile'),


    path('',views.index),
   # path('index/',views.index,name='index'),
    path('',views.s18s),
    path('cgpa/',views.cgpa,name='cgpa'),
    path('2017_scheme-1st_sem/',views.s17s1,name='s17s1'),
    path('',views.s17s2),
    path('',views.s17s3),
    path('',views.s17s4),
    path('',views.s17s5),
    path('',views.s17s6),
    path('',views.s17s7),
    path('',views.s17s8),
    path('sgpa/',views.sgpa,name='sgpa'),

]

from django.contrib import admin
from django.urls import path,include
from nnn import views
from nnn.views import home,proo_view,su_b

urlpatterns = [
    path('', views.home),
    path('create',views.proo_view),
    path('saaa',views.su_b),
    

    ]
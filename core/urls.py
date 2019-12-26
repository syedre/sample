from django.contrib import admin
from django.urls import path,include
from core import views
from core.views import Homepageview,save

urlpatterns = [
    path('', Homepageview,name='home'),
    path('save',views.save),
]
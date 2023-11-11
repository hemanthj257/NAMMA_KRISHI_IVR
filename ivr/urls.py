from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ivr_welcome, name='ivr_welcome'),
    path('gather_1/', views.gather_1, name='gather_1'),
    path('gather_locality/', views.gather_locality, name='gather_locality'),
    path('gather_brand/', views.gather_brand, name='gather_brand'),
    path('gather_type/', views.gather_type, name='gather_type'),
    path('connect_farming_vehicle/', views.connect_farming_vehicle, name='connect_farming_vehicle'),
    path('connect_attachments/', views.connect_attachments, name='connect_attachments'),
]

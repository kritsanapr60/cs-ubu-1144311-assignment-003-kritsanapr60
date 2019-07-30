from django.contrib import admin
from django.urls import path
from commathweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('dec_32/',views.dec_32),
    path('dec_64/',views.dec_64),
    path('solve/',views.datasolve),
]

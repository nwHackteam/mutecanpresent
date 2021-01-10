from django.contrib import admin
from django.urls import path,include
from app import views as app_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app_views.home, name='home'), 

]
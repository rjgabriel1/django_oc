"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_add, name='band-add'),
    path('bands/<int:band_id>/update/', views.band_update, name='band-update'),
    path('bands/<int:band_id>/delete/', views.band_delete, name='band-delete'),


    path('merchs/', views.merch_list, name='merch-list'),
    path('merchs/<int:merch_id>/', views.merch_detail, name='merch-detail'),
    path('merchs/add', views.merch_add, name='merch-add'),
    path('merchs/<int:merch_id>/update/', views.merch_update, name='merch-update'),
    path('merchs/<int:merch_id>/delete/', views.merch_delete, name='merch-delete'),

]

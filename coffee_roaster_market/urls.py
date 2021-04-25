"""coffee_roaster_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers

from .apps.coffee import views


router = routers.DefaultRouter()
router.register(
    r"sensorial_profiles", views.SensorialProfileViewSet, basename="sensorial_profiles"
)
router.register(r"geolocations", views.GeolocationViewSet, basename="geolocations")
router.register(r"plantations", views.PlantationViewSet, basename="plantations")
router.register(r"coffee", views.CoffeeViewSet, basename="coffee")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]

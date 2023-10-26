"""
URL configuration for VehiculeManagment project.

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Backend.views import VehiculeViewSet, FullTankViewSet, InterventionViewSet, FullTankIDViewSet, IntervetionIDViewSet

router = DefaultRouter()
router.register(r'vehicules', VehiculeViewSet)
router.register(r'fulltanks', FullTankViewSet)
router.register(r'interventions', InterventionViewSet)
# router.register(r'fulltanks', FullTankIDViewSet)
# router.register(r'interventions', IntervetionIDViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

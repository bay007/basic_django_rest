"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mascota.urls import URL_PATTERNS
from refugio.views import index
from rest_framework import routers
from api.views import (PersonaViewSet, MascotaViewSet, VacunaViewSet)


router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'mascota', MascotaViewSet)
router.register(r'vacuna', VacunaViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
)

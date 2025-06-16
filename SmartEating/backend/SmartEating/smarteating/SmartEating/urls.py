"""SmartEating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from smartEatingApp.api import views as api_views
from django.views.generic import TemplateView
from smartEatingApp.api.views import *

router = routers.DefaultRouter()

urlpatterns = [
   path('api/', include('djoser.urls')),
   path('api/', include('djoser.urls.authtoken')),
   path('api/', include(router.urls)),
   path('api/user/', UserDetailView.as_view(), name='user-detail'),
   path('api/user/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
   path('api/user/crear-receta/', PlatoCreateView.as_view(), name='crear-plato'),
   path('api/listplatos/', PlatosListAPIView.as_view(), name='platos-usuario'),
   path('api/getplato/<int:pk>/', PlatoDetailAPIView.as_view(), name='plato-detail'),
   path('api/deleteplato/<int:pk>/', PlatoDeleteAPIView.as_view(), name='plato-delete'),
   path('api/listaingredientes/', ContarIngredientesView.as_view(), name='contar_ingredientes'),
   path('api/dates/', YearPlatosAPIView.as_view(), name='anios-platos'),
   path('api/platos/<int:year>/', PlatosPorMesView.as_view(), name='platos_por_mes'),
   path('admin/', admin.site.urls),
]

#urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
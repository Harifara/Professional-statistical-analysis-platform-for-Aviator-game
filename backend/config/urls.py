"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from apps.rounds.views import RoundViewSet, StatisticsViewSet
from apps.analytics.views import AnalyticsViewSet, AnomalyViewSet
from apps.predictions.views import PredictionViewSet
from apps.alerts.views import AlertViewSet, AlertConfigViewSet
from apps.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'rounds', RoundViewSet, basename='round')
router.register(r'statistics', StatisticsViewSet, basename='statistics')
router.register(r'analytics', AnalyticsViewSet, basename='analytics')
router.register(r'anomalies', AnomalyViewSet, basename='anomaly')
router.register(r'predictions', PredictionViewSet, basename='prediction')
router.register(r'alerts', AlertViewSet, basename='alert')
router.register(r'alert-configs', AlertConfigViewSet, basename='alert-config')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('apps.users.urls')),
    
    # Swagger/OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

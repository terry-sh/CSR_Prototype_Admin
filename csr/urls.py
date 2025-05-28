"""
URL configuration for csr project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from activity.views import ActivityViewSet, ActivityEnrollViewSet, ActivityEventViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # ----- Auth API ----- #
    path('api/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # ----- Activity API ----- #
    path('api/activity/newest', ActivityViewSet.as_view({
        'get': 'newest',
    })),
    path('api/activity/all', ActivityViewSet.as_view({
        'get': 'all',
    })),
    # Enroll Activity
    path('api/activity/enroll/<int:activity_id>', ActivityEnrollViewSet.as_view({
        'post': 'enroll',
    })),
    # Event list
    path('api/activity/<int:activity_id>/events', ActivityEventViewSet.as_view({
        'get': 'all_events',
    })),
    # Activity detail
    path('api/activity/<int:activity_id>', ActivityViewSet.as_view({
        'get': 'detail',
    })),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
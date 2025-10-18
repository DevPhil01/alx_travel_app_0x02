#!/usr/bin/env python3
"""
URLs for Listings app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, welcome

# Router for API endpoints
router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', welcome, name='welcome'),
    path('api/', include(router.urls)),  # ✅ All API endpoints under /api/
]

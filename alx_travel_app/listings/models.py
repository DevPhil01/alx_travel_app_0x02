#!/usr/bin/env python3
"""
Models for Listings, Bookings, and Reviews
"""

import uuid
from django.db import models
from django.conf import settings


class Listing(models.Model):
    """A property or travel listing."""
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    location = models.CharField(max_length=255, null=False)
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="listings"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """A booking for a listing."""
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField(null=False)
    check_out = models.DateField(null=False)
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.booking_id} for {self.listing.title}"


class Review(models.Model):
    """A review left by a user for a listing."""
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()  # e.g., 1–5
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1) & models.Q(rating__lte=5), name="valid_rating")
        ]

    def __str__(self):
        return f"Review {self.rating} for {self.listing.title}"

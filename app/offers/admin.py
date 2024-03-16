from django.contrib import admin

# Register your models here.

from .models import Offer, OfferStatus

admin.site.register(OfferStatus)
admin.site.register(Offer)

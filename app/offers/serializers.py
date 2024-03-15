from rest_framework import serializers

from .models import Offer


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ['id', 'created_by', 'user_payment_method_id', 'amount', 'offer_type', 'is_active']
        read_only_fields = ['id', 'created_at']

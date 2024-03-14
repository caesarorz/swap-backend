from rest_framework import serializers

from .models import PaymentMethod

class PaymentMethodSerializer(serializers.ModelSerializer):
    """Serializer for the payment object."""

    class Meta:
        model = PaymentMethod
        fields = ['id', 'name', 'is_active']
        read_only_fields = ['id']


class PaymentMethodDetailSerializer(PaymentMethodSerializer):
    """Serializer for detail payment view."""

    class Meta(PaymentMethodSerializer.Meta):
        fields = PaymentMethodSerializer.Meta.fields + [
            'description',
            'created_by',
            'created_at',
            'updated_at'
        ]
from rest_framework import serializers

from .models import PaymentMethod, PaymentMethodUser

class PaymentMethodSerializer(serializers.ModelSerializer):
    """Serializer for payment object."""

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


class UserPaymentMethodSerializer(serializers.ModelSerializer):
    """Serializer for user payment methods."""

    class Meta:
        model = PaymentMethodUser
        fields = ['id', 'payment_method_name_id', 'payment_method', 'user', 'is_active']
        read_only_fields = ['id']


class UserPaymentMethodDetailSerializer(UserPaymentMethodSerializer):
    """Serializer for detail user payment method view."""

    class Meta(UserPaymentMethodSerializer.Meta):
        fields = UserPaymentMethodSerializer.Meta.fields + [
            'created_at',
            'updated_at'
        ]
from rest_framework import serializers

from .models import PaymentMethod

class PaymentMethodSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = PaymentMethod
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    # def create(self, validated_data):
    #     """Create and return a user with encrypted password."""
    #     return PaymentMethod.objects.create_user(**validated_data)

    # def update(self, instance, validated_data):
    #     """Update and return user."""
    #     password = validated_data.pop('password', None)
    #     user = super().update(instance, validated_data)

    #     if password:
    #         user.set_password(password)
    #         user.save()

    #     return user
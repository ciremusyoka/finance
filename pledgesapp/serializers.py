from rest_framework import serializers
from .models import PledgePurpose, AllPledges


# pledges purpose serializer
class PledgePurposeSerializer(serializers.ModelSerializer):
    amount_paid = serializers.DecimalField(allow_null=True, decimal_places=2, read_only=True, max_digits=1000000)
    class Meta:
        model = PledgePurpose
        fields = ('__all__')


# register pledges serializer
class AllPledgesSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(decimal_places=2, allow_null=True, max_digits=1000000, read_only=True)
    amount_paid = serializers.DecimalField(decimal_places=2, allow_null=True, max_digits=1000000, read_only=True)

    class Meta:
        model = AllPledges
        fields = ('__all__')

    def create(self, validated_data):
        pledge_amount = validated_data.get('pledge_amount', None)
        initial_payment = validated_data.get('initial_payment', None)
        instance = self.Meta.model(**validated_data)
        instance.amount_paid = initial_payment
        if initial_payment is None or '':
            instance.balance = pledge_amount
        else:
            instance.balance = pledge_amount - initial_payment
        instance.save()
        return instance
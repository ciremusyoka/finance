from rest_framework import serializers
from .models import loans
from .payments.serializers import PaymentsSerializer

class CreateLoansSerializer(serializers.ModelSerializer):
    balance = serializers.CharField(read_only=True)
    class Meta:
        model = loans
        fields = ('__all__')

    def create(self, validated_data):
        amount = validated_data.get('amount', None)
        instance = self.Meta.model(**validated_data)
        if amount is not None:
            instance.balance = validated_data.get('amount', None)
        instance.save()
        return instance

class ListLoanSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(many=True, read_only=True)
    class Meta:
        model = loans
        fields = ('payments','amount', 'balance', 'owner', 'created', 'updated')
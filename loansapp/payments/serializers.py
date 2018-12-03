from rest_framework import serializers
from ..models import payments, loans

class PaymentsSerializer(serializers.ModelSerializer):
    balance = serializers.CharField(read_only=True)
    interest = serializers.CharField(read_only=True)
    owner = serializers.CharField(read_only=True)
    class Meta:
        model = payments
        fields = ('__all__')

    def create(self, validated_data):
        amount_paid = validated_data.get('amount_paid', None)
        loan = validated_data.get('loan', None)
        d = str(loan)
        loan_details = loans.objects.get(id=d)
        instance = self.Meta.model(**validated_data)
        instance.owner = loan_details.owner
        if amount_paid is not None:
            old_bal = loan_details.balance
            if old_bal is None:
                interest = 0
                instance.interest = interest
                old_bal = 0
            else:
                interest = old_bal*0.1
            if amount_paid > old_bal:
                content = 'your payment is more than your current balance of: %s' %old_bal
                raise serializers.ValidationError(content)

            elif amount_paid == interest:
                instance.balance = old_bal

            elif amount_paid <= old_bal:
                bal = old_bal - amount_paid
                balance_per = bal*0.1
                instance.interest = balance_per
                new_balance = bal + balance_per
                instance.balance = new_balance
        instance.save()
        return instance

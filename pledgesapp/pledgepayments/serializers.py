from rest_framework import serializers
from ..models import AllPledges,PledgePayments


# pay pledges serializer
class PledgesPaymentSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(decimal_places=2, read_only=True, max_digits=1000000)
    all_totals = serializers.DecimalField(decimal_places=2, read_only=True, max_digits=1000000)
    totals = serializers.DecimalField(decimal_places=2, read_only=True, max_digits=1000000)

    class Meta:
        model = PledgePayments
        # exclude = ('all_totals', 'totals')
        fields = ('__all__')

    def create(self, validated_data):
        pledge = validated_data.get('pledge', None)
        amount = validated_data.get('amount_paid', None)
        instance = self.Meta.model(**validated_data)
        number = PledgePayments.objects.filter(pledge=str(pledge)).count()
        current_pledge = AllPledges.objects.get(id=str(pledge))
        pledgeamount = current_pledge.pledge_amount

        if number == 0:
            instance.balance = pledgeamount - amount
            alltotals = amount
            instance.all_totals = alltotals
            totals = amount
        else:
            payments = PledgePayments.objects.filter(pledge=str(pledge))
            oldamount = 0
            for amt in payments:
                oldamount += amt.amount_paid
            totals = oldamount + amount
            instance.balance = pledgeamount - (oldamount + amount)
        instance.totals = totals
        print(totals)
        all = PledgePayments.objects.all()
        mytotal = 0
        for t in all:
           mytotal += t.amount_paid
        alltotals = mytotal + amount
        instance.all_totals = alltotals
        print(alltotals)
        instance.save()
        return instance
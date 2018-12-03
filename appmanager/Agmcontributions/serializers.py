import datetime
from rest_framework import serializers
from ..models import AGMBalances, AGMContributions

class AGMContributionSerializer(serializers.ModelSerializer):
    balance = serializers.CharField(read_only=True)
    year = serializers.CharField(allow_blank=True)
    payments = serializers.CharField(read_only=True)
    overdue = serializers.CharField(read_only=True)
    class Meta:
        model = AGMContributions
        fields = ('__all__')

    def create(self, validated_data):
        year = validated_data.get('year', None)
        owner = validated_data.get('owner', None)
        amount_paid = validated_data.get('amount_paid', None)
        instance = self.Meta.model(**validated_data)
        if year is None or year is '':
            now = datetime.datetime.now()
            instance.year = now.year
            contributions = AGMContributions.objects.filter(owner=owner, year=now.year).count()
            instance.payments = contributions
        else:
            contributions = AGMContributions.objects.filter(owner=owner, year=year).count()
            instance.payments = contributions
            instance.year = year
        if contributions == 0:
            instance.balance = 2000-amount_paid
        else:
            contributions_object = AGMContributions.objects.filter(owner=owner, year=instance.year)
            total_amount = 0
            for obj in contributions_object:
                total_amount = total_amount + obj.amount_paid
            balance = 2000-(amount_paid+total_amount)
            instance.balance = balance
        if instance.balance < 0:
            instance.overdue = instance.balance*-1
        else:
            instance.overdue = 0
        instance.save()
        return instance


class AGMBalancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AGMBalances
        fields = ('__all__')

        # data = serializers.serialize('json', list(contributions_object), fields=('fileName', 'id'))
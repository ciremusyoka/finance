from rest_framework import serializers
from .models import MyUser, members

class CreateUserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    sir_name = serializers.CharField(required=True)
    # dob = serializers.DateField(required=True)


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'password', 'sir_name', 'first_name', 'last_name', 'gender', 'dob')


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = members
        fields = ('__all__')
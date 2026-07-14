from rest_framework import serializers
from django.contrib.auth.models import User

# class UserAuthSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True, max_length=150)
#     password = serializers.CharField()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )
    password_confirm = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'password_confirm',
        ]
        read_only_fields = ['id']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                'password_confirm': 'Пароли не совпадают.'
            })

        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')

        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
                                            write_only=True,
                                            style={'input_type': 'password'}
                                        )
    password_2 = serializers.CharField(
                                            write_only=True,
                                            style={'input_type': 'password'}
                                        )
    class Meta:
        model = User
        fields = ['username','email','password','password_2']
    
    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password_2')

        if password1 != password2:
            raise serializers.ValidationError("Пароли не совпадают.")

        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        return user
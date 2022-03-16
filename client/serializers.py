from dataclasses import fields
from rest_framework import serializers
from .models import User
from  rest_framework.validators import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import check_password

class RegisterSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=120, write_only=True)
    class Meta:
        model = User
        fields = ("username", 'phone', "email", 'password', 'confirm')
        extra_kwargs = {
            'password': {'write_only': True}
            # "is_active":{"write_only":True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise ValidationError(_("Parol va parolni tasdiqlash noto'g'ri!"))
        return attrs
    
    def create(self, validated_data):
        user = User(
        username=validated_data['username'],
        # email=validated_data['email'],
        phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", 'phone', 'email', 'first_name', 'last_name', 'photo')


class PswdChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, write_only=True)
    new = serializers.CharField(max_length=20, write_only=True)
    confirm = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ("password", "new", "confirm")   

    def validate(self, data):
        if  data.get('password')==None or data.get('new')==None or data.get('confirm')==None:
            raise ValidationError(_("Qatorlar to'ldirilishi shart!"))

        currentpswd = self._context['request'].user.password
        pswd_checked = check_password(data.get('password'), currentpswd)
        if not pswd_checked:
            raise ValidationError(_("Eski parol noto'g'ri!"))
        
        if data['new'] != data['confirm']:
            raise ValidationError(_("Yangi parolni tasdiqlash to'g'ri kelmadi!"))
        
        return data
    
    def update(self,instance, validated_data):
        user = instance
        user.set_password(validated_data['new'])
        user.save()
        return user
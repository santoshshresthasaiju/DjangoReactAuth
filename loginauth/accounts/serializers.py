from .models import *
from rest_framework import serializers
from .helpers import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'password' , 'phone']
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        phone = validated_data['phone']
        
        user = User.objects.create(email=email, phone=phone)
        user.set_password(password)
        send_otp_to_mobile(phone , user)
        user.save()
        return user
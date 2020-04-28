from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model


#SUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MitaalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mitaala
        fields = '__all__'  # ('id','title')

class DarasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Darasa
        fields ='__all__'

class UmahiriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Umahiri
        fields = '__all__'

class UmahsusiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Umahsusi
        fields = '__all__'

class MuhulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muhula
        fields = '__all__'

class JumaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juma
        fields = '__all__'

class SikuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siku
        fields = '__all__'

class ShughuliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shughuli
        fields = '__all__'

class VipindiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vipindi
        fields = '__all__'

class MtaalaHeadSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = MtaalaHead
        fields = '__all__'
        extra_kwargs = {'articles': {'required': False}}

class MtaalaArticleSerializer(serializers.ModelSerializer):
    headers = MtaalaHeadSerializer(many=True, read_only=True)

    class Meta:
        model = MtaalaArticles
        fields= '__all__'
        extra_kwargs = {'headers': {'required': False}}

class RegistrationSerializer(serializers.ModelSerializer):
    repassword = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model=User
        fields=['email', 'username', 'password','repassword']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        user=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password =self.validated_data['password']
        repassword=self.validated_data['repassword']

        if password != repassword:
            raise serializers.ValidationError({'password':'Password must Match'})
        user.set_password(password)
        user.save()
        return user

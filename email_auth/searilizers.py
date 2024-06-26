from rest_framework import serializers
from .models import *

class Color_searilizer(serializers.ModelSerializer):
    class Meta:
        model =  Color
        fields = ['color_name']


class Mail_searilizer(serializers.ModelSerializer):
    color = Color_searilizer()
    country = serializers.SerializerMethodField()

    def get_country(self, obj):
        return {'data': 'test'}
    class Meta:
        model = Mail
        fields = '__all__'
        # depth = 1

class login_serilizer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
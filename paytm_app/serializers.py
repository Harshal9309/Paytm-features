
from rest_framework import serializers
from .models import UserProfile, Investment,ShoppingAssistant,Chatbox

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class InvestmentSerializer(serializers.ModelSerializer):
    # user = UserProfileSerializer()
    class Meta:
        model = Investment
        fields = '__all__'


class ShoppingAssistantSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = ShoppingAssistant
        fields = '__all__'


class ChatboxSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer() 
    class Meta:
        model = Chatbox
        fields = '__all__'

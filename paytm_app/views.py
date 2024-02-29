
from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, Investment
from .serializers import UserProfileSerializer, InvestmentSerializer,ShoppingAssistant,ShoppingAssistantSerializer,Chatbox,ChatboxSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class ShoppingAssistantViewSet(viewsets.ModelViewSet):
    queryset = ShoppingAssistant.objects.all()
    serializer_class = ShoppingAssistantSerializer


class ChatboxViewSet(viewsets.ModelViewSet):
    queryset = Chatbox.objects.all()
    serializer_class = ChatboxSerializer

def home_view(request):
    return render(request, 'home.html')

def shopping_assistant_form_view(request):
    return render(request, 'shopping_assistant_form.html')

def chatbox_form_view(request):
    return render(request, 'chatbox_form.html')
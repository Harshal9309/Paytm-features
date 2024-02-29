
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, InvestmentViewSet,ShoppingAssistantViewSet,ChatboxViewSet,home_view,shopping_assistant_form_view,chatbox_form_view

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'investments', InvestmentViewSet)
router.register(r'shoppingassistants', ShoppingAssistantViewSet)
router.register(r'chatboxes', ChatboxViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('', home_view, name='home'),
    path('shopping_assistant/', shopping_assistant_form_view, name='shopping_assistant_form'),
    path('chatbox/', chatbox_form_view, name='chatbox_form'),
]

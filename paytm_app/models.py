
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    shopping_preferences = models.TextField(null=True, blank=True)

class Investment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    investment_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.investment_type}"



class ShoppingAssistant(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    preferences = models.TextField()
    trending_products = models.TextField()


class Chatbox(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

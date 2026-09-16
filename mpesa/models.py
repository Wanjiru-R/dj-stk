from django.db import models

# Create your models here.
class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    checkout_id = models.CharField(max_length=100, unique=True)
    mpesa_code = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, default='Pending')


    def __str__(self):
        return f"{self.mpesa_code} - {self.amount} KES"
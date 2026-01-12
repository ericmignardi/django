from django.db import models

# Create your models here.

class GrainPrice(models.Model):
    grain_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.grain_type}: ${self.price}"
    
class ChatMessage(models.Model):
    role = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
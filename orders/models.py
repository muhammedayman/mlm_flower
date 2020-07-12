from django.db import models
from staff.models import Staff
from miscapp.models import BaseModel

# Create your models here.
class Orders(BaseModel):
    user_staff=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="user_staff")
    user_distributer=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="user_distributer")
    user_delivery=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="user_delivery")
    product_id=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    ratings=models.PositiveIntegerField()
    price=models.FloatField(default=0)
    net_amout=models.FloatField(default=0)
    gross_amount=models.FloatField(default=0)
    tax=models.FloatField(default=0)
    offer=models.FloatField(default=0)
    date_order=models.DateTimeField(null=True, blank=True)
    date_dispatch=models.DateTimeField(null=True, blank=True)
    is_returned=models.BooleanField(default=False)
    
    class Meta:
        db_table = 'orders'

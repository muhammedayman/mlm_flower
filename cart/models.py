from django.db import models
from miscapp.models import BaseModel
from staff.models import Staff

class Cart(BaseModel):
    user_staff=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="cart_staff")
    user_customer=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="cart_customer")
    user_delivery=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="cart_delivery")
    product_id=models.PositiveIntegerField()
    price=models.FloatField(default=0)
    date_order=models.DateTimeField(null=True, blank=True)
    date_dispatch=models.DateTimeField(null=True, blank=True)
    is_returned=models.BooleanField(default=False)
 
    class Meta:
        db_table = 'carts'
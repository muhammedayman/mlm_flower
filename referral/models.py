from django.db import models
from miscapp.models import BaseModel
from staff.models import Staff
from django.contrib.auth.models import User

class Refer(BaseModel):
    staff=models.OneToOneField(Staff, on_delete=models.CASCADE)
    referal_username=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="referal_username")
    amount=models.FloatField()
    referal_level=models.PositiveIntegerField()
    referal_up=models.PositiveIntegerField(default=0)
    referal_down=models.PositiveIntegerField(default=0)
    refer_amount=models.FloatField(default=0)
    total_amount=models.FloatField(default=0)
    transfered_amount=models.FloatField(default=0)
    referal_code=models.CharField(max_length=50,null=True, blank=True)
    transaction_code=models.CharField(max_length=200,null=True, blank=True)
    transaction_date=models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'refer'


    


    


from django.db import models
from staff.models import Staff
from miscapp.models import BaseModel



# Create your models here.
class Tracker(BaseModel):
    user_staff=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="tracker_staff")
    user_distributer=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="tracker_distributer")
    user_delivery=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="tracker_delivery")
    bill_number=models.CharField(max_length=100,null=True, blank=True)
    locations=models.CharField(max_length=100,null=True, blank=True)
    date_order=models.DateTimeField(null=True, blank=True)
    date_dispatch=models.DateTimeField(null=True, blank=True)
    out_of_delivery=models.BooleanField(default=False)
    
    class Meta:
        db_table = 'trackers'    
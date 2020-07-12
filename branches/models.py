from django.db import models

# Create your models here.
from django.contrib.contenttypes.fields import GenericRelation
from miscapp.models import BaseModel
from agencies.models import Agency
from staff.models import Staff
# from trips.models import Trip


class Branch(BaseModel):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=12, unique=True)
	agency = models.ForeignKey(Agency, on_delete=models.PROTECT, db_column='agency_code', to_field='code')
	contact_person_name = models.CharField(max_length=50)
	address = models.TextField(null=True, blank=True)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	phone_number = models.CharField(max_length= 15)
	email = models.CharField(max_length=50)
	state = models.CharField(max_length=25)
	city = models.CharField(max_length=25)
	active = models.BooleanField(default = True)

	staff = GenericRelation(Staff)
	# trips = GenericRelation(Trip, related_query_name='branch', content_type_field='owner_type', object_id_field='owner_id')

	class Meta:
		db_table = 'branches'

	def __str__(self):
		return self.name
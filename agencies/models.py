from django.db import models
from miscapp.models import BaseModel
from staff.models import Staff


class Agency(BaseModel):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=12, unique=True)
	website = models.CharField(max_length=100)
	description = models.TextField()

	class Meta:
		db_table = 'angencies'

	def __str__(self):
		return self.name
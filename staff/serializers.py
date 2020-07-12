from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import ContentType, User
from .models import Staff
from agencies.models import Agency
# from branches.models import Branch
import pdb

class StaffSerializer(serializers.ModelSerializer):
	employer_type = serializers.CharField(source='employer_content_type.model')
	employer_name = serializers.CharField(source='employer.name')

	class Meta:
		model = Staff
		fields = ('id', 'name', 'email', 'phone_number','employer_type', 'employer_id', 'employer_name', "role")

class StaffCreateSerializer(serializers.ModelSerializer):
	username = serializers.CharField(write_only= True)
	password = serializers.CharField(write_only= True)
	employer_code = serializers.CharField(write_only= True, required=False)
	employer_type = serializers.CharField(write_only= True)

	class Meta:
		model = Staff
		fields = ('name', 'email', 'phone_number','username', 'password', 'employer_code', 'employer_type', 'employer_id', "role")
		extra_kwargs = {'employer_id': {'required': False}, 'employer': {'required': True}}

	def validate(self, attrs):
		attrs = self.add_employer(attrs)
		attrs = super().validate(attrs)
		user = User.objects.filter(username=attrs.get('username')).first()
		if user:
			raise serializers.ValidationError({'username': ["User already exists"]})
		if not attrs.get('employer', None):
			raise serializers.ValidationError({'employer': ["Employer required"]})
		return attrs

	def add_employer(self, attrs):
		employer_code = attrs.pop('employer_code', None)
		if employer_code:
			employer = Agency.objects.filter(code=employer_code).first()
			employer = employer or Branch.objects.filter(code=employer_code).first()
		else:
			employer = ContentType.objects.get(model=attrs.pop('employer_type', None)).get_object_for_this_type(id=attrs.pop('employer_id', None))
		attrs.update({'employer': employer})
		return attrs

class LoginSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)
		return token

	def validate(self, attrs):
		data = super(LoginSerializer, self).validate(attrs)
		data.update({'staff': StaffSerializer(self.user.staff).data})
		return data


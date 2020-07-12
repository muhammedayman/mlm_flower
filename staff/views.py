from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from .models import Staff
from .serializers import LoginSerializer, StaffSerializer, StaffCreateSerializer
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class DynamicSearchFilter(filters.SearchFilter):
	def get_search_fields(self, view, request):
		return request.GET.getlist('search_fields', ['role','name'])   
	
class Login(TokenObtainPairView):
    serializer_class = LoginSerializer

class StaffViewSet(viewsets.ModelViewSet):
	queryset = Staff.objects.all()
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	filterset_fields = ['role']
	search_fields = ['^name']

	def get_serializer_class(self):
		if self.action == 'create':
			return StaffCreateSerializer
		return StaffSerializer


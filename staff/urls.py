from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'staff', StaffViewSet, basename='branches')
urlpatterns = [
	path('staff/login/', Login.as_view(), name='login' ),
]
urlpatterns += router.urls
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import RegisterView, dashboard, MyTokenObtainPairView

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenObtainPairView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("dashboard/", dashboard, name="dashboard"),
]
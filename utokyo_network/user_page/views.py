from django.shortcuts import render
from .models import User, Profile
from .serializer import UserSerializer, RegisterSerializer, TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):  
  queryset = User.objects.all()
  permission_classes = [AllowAny]
  serializer_class = RegisterSerializer



@api_view(['GET', "POST"])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == "GET":
        response = f"Hello {request.user.username}, you are seeing a GET response!"
        return Response({"response": response}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        text = request.POST.get("text")
        reponse = f"Hey {request.user.username}, You sent a POST request with the text: {text}"
        return Response({"response": response}, status=status.HTTP_200_OK)
    else:
        return Response({"response": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', "POST"])
@permission_classes([IsAuthenticated])
def testEndpoint(request):
    if request.method == "GET":
        response = f"Congratulation {request.user}, your API ijust responded to GET request!"
        return Response({"response": response}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        text = request.POST.get("text")
        reponse = f"Hey {request.user}, You sent a POST request with the text: {text}"
        return Response({"response": response}, status=status.HTTP_200_OK)
    else:
        return Response({"response": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)    
    
# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)

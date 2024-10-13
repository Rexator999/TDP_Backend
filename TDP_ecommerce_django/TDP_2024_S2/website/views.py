from django.shortcuts import render, redirect
from .models import Client, Seller, ClientRequest, SellerProduct
from django.contrib.auth import logout, authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, permissions, status
from .serializers import ClientRequestSerializer, ClientSerializer, SellerSerializer, SellerProductSerializer, ClientLoginSerializer, ClientRegisterSerializer

class ClientHomeView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Welcome to the home page!"}, status=status.HTTP_200_OK)

class ClientRegisterView(generics.CreateAPIView):
    serializer_class = ClientRegisterSerializer
    permission_classes = [AllowAny]

class ClientLoginView(generics.GenericAPIView):
    serializer_class = ClientLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        # Attempt to authenticate the user
        user = authenticate(email=email, password=password)

        # Logging the outcome of the authentication
        if user is not None:
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            print(f"Login failed for email: {email}. Check if user exists and the password is correct.")
            return Response({"message": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

# ClientRequest Views
class ClientRequestListCreateView(generics.ListCreateAPIView):
    queryset = ClientRequest.objects.all()
    serializer_class = ClientRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

class ClientRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientRequest.objects.all()
    serializer_class = ClientRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

class SellerListCreateView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.AllowAny]

class SellerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]

class SellerProductListCreateView(generics.ListCreateAPIView):
    queryset = SellerProduct.objects.all()
    serializer_class = SellerProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class SellerProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SellerProduct.objects.all()
    serializer_class = SellerProductSerializer
    permission_classes = [permissions.IsAuthenticated]

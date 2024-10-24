from django.shortcuts import render, redirect
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Service, Booking, Review
from .serializers import ServiceSerialzier, BookingSerialzier, ReviewSerializer, RegisterSerializer, LoginSerializer
from .permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter()
    serializer_class = ServiceSerialzier


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerialzier

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def perform_create(self, serializer):
        reception_date = serializer.validated_data['reception_date']
        reception_time = serializer.validated_data['reception_time']
        if Booking.objects.filter(reception_date=reception_date, reception_time=reception_time).exists():
            raise serializers.ValidationError("Данное время уже занято.")
        serializer.save(user=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def home(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, "home.html", context)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

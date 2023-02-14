
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView


from .serializers import RegisterSerializer, LoginSerializer, UserSerializer,ImageUploadSerializer, ImageSerializer
from django.contrib.auth.models import User
from .models import  Profile, Image, Interest

def hello(request):
    return HttpResponse("Hello World")

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = {
            "message": "User registered successfully"
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

class ImageUploadView(APIView):

    def post(self, request, format=None):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            profile = Profile.objects.get(user=request.user)
            image = Image(image=serializer.validated_data['image'])
            image.save()
            profile.images.add(image)
            profile.save()
            return Response(ImageSerializer(image).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
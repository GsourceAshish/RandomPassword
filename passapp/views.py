
from django.conf import settings
from .serializers import UserSerializer,ChangePasswordSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics
from rest_framework import status
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework.serializers import Serializer



class RegisterView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    authentication_classes = [BasicAuthentication,]
    
   

class ChangePasswordAPI(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        
        serializer_class = ChangePasswordSerializer
        model = CustomUser
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

                if serializer.data.get('confirm_password') != serializer.data.get('new_password'):
                    raise serializers.ValidationError({'password': 'Password must be confirmed correctly.'})
                
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                return Response("Success.", status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    



  
    # def create(self, request, *args, **kwargs):
    #     response = super(RegisterView, self).create(request, *args, **kwargs)
    #     send_mail()  # sending mail
    #     return response

    # def create(self, request):
    #     serializer = UserSerializer(
    #     data=request.data)
    #     serializer.is_valid(raise_exception=True)
       
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
  #return Response(UserSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


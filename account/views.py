from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView 
from account.serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate   # to authenticate while login


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Register successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     {
#     "email":"sushant@gmail.com",
#     "name":"Sushant Gondukupi",
#     "mobile":"9970603429",
#     "password":"Sushant@123",
#     "password2":"Sushant@123"

# }
    


# User Login
class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            user = authenticate(email=email, password=password)#to authenticate while login
            if user is not None:
                return Response({'msg':'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_fields_errrors':['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
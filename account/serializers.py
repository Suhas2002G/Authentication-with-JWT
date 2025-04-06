from rest_framework import serializers 
from account.models import User 
from account.user_manager import UserManager


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta: 
        model = User 
        fields = ['email', 'name', 'password', 'password2', 'mobile']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    # Validating Password and Confirm Password while Registering
    # Here attrs is nothing but data coming from frontend
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('Password and Confirm Password does not matched')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    



# User Login
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta : 
        model = User 
        fields = ['email', 'password']

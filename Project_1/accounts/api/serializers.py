from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class LogINSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True,style={'input_type':'password'},write_only=True)




class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password',
            'password2']
        #extra_kwargs = {'password':{'write_only':True}}

    def validate(self, data):
        pw = data.get('password')
        pw2= data.pop('password2')
        if pw !=pw2:
            raise serializers.ValidationError('pasword does not match')
        return data

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact = value)
        if qs.exists():
            return serializers.ValidationError('email id already register')
        return value

    def validate_name(self, value):
        qs = User.objects.filter(username__iexact = username)
        if qs.exists():
            return serializers.ValidationError('username id already register')
        return value

    def create(self,validated_data):
        print(validated_data)
        user_obj = User(
            username = validated_data.get('username'),
            email = validated_data.get('email')
            )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return validated_data


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True,style={'input_type':'password'},write_only=True)
    new_password = serializers.CharField(required=True,style={'input_type':'password'},write_only=True)

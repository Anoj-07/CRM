from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, error_messages={
                                     "required": "Username can not be blank."})
    first_name = serializers.CharField(max_length=30, error_messages={
                                       "required": "First name is required cannot be blank"})
    last_name = serializers.CharField(max_length=30, error_messages={
                                      "required": "Last name is required cannot be blank"})
    email = serializers.EmailField(error_messages={
                                   "required": "Email is required", "invalid": "Enter a valid email address.", })
    password = serializers.CharField(write_only=True, min_length=8, error_messages={
                                     "required": "Password is required must be 8 digit."})

    # field level validation
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already exits.")
        return value

    def valdate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exits.")
        return value

    # object level validation
    def validate(self, data):
        username = data['username']
        password = data['password']

        if username.upper() == password.upper():
            raise serializers.ValidationError("username and password must not be same")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user

from rest_framework import serializers
from .models import Books
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'  # Includes all fields: name, author, and price





class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def create(self, validated_data):  
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  
        user.save()
        return user

    



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data["email"]
        password = data["password"]

        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            return {"user": user}

        raise serializers.ValidationError("Invalid email or password.")


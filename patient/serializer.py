from rest_framework import serializers
from . import models
from django.contrib.auth.models import User



class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'




class RegistrationSerializer(serializers.ModelSerializer):
    confirm_passwoord = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_passwoord']


    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_passwoord = self.validated_data['confirm_passwoord']

        if password != confirm_passwoord:
            raise serializers.ValidationError({'error':'Password did not match.'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':'This email address already exists.'})
        
        account = User(username=username, email=email)
        account.set_password(password)
        account.is_active = False # make it true when user click our varification email
        account.save()
        return account

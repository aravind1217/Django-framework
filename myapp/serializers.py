from rest_framework import serializers
from .models import Friend
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class FriendSerializer(serializers.ModelSerializer):
	class Meta:
		model = Friend
		fields = ['id','first_name','last_name','dob','mobile_no','email','location']


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username','password']


		extra_kwargs ={'password':{

		 'write_only':True,
		 'required' : True
		}}


	def create(self,validated_data):
		user = User.objects.create_user(**validated_data)
		Token.objects.create(user=user)
		return user


from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import FriendSerializer,UserSerializer
from .models import Friend
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.authtoken.views import Token

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

class FriendViewSet(viewsets.ModelViewSet):
	serializer_class = FriendSerializer
	queryset = Friend.objects.all()


class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
	serializer_class = FriendSerializer
	queryset = Friend.objects.all()

	lookup_field = 'id'
	authentication_classes=[TokenAuthentication]
	permission_classes= [IsAuthenticated]

	def get(self,request,id= None):
		if id:
			return self.retrieve(request,id)
		else:
			return self.list(request)
	def post(self,request):
		return self.create(request)

	def put(self, request, id = None):
		return self.update(request,id)

	def delete(self, request, id=None):
		return self.destroy(request,id)

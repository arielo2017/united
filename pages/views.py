from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import users
from . models import matchmaking
from . serializers import usersSerializer
from . serializers import matchSerializer

def index(request):
    return render(request, 'index.htlm')

def about(request):
    return render(request, 'about.htlm')


class usersList(APIView):

    def get(self, request):
        users1 =  users.objects.all()
        serializer = usersSerializer(users1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class matchMakingList(APIView):

    def get(self, request):
        matches1 = matchmaking.objects.all()
        serializer = matchSerializer(matches1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

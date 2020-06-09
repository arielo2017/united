from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import users
from . models import matchmaking
from . models import training
from . serializers import usersSerializer
from . serializers import matchSerializer
from . serializers import trainingSerializer
import json

def index(request):
    return render(request, 'pages/index.htlm')

def about(request):
    return render(request, 'pages/about.htlm')


class usersList(APIView):

    def get(self, request):
        users1 = users.objects.all()
        serializer = usersSerializer(users1, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class trainingList(APIView):

    def get(self, request):
        training1 = training.objects.all()
        serializer = trainingSerializer(training1, many=True)
        return Response(serializer.data)

    def post(self,request):
        print('reading....')
        print('converted:', json.dumps(request.data))
        
        try:
            serializer = trainingSerializer(data=request.data)
            print('serializer....', serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            print(Exception)

class matchMakingList(APIView):

    def get(self, request):
        matches1 = matchmaking.objects.all()
        serializer = matchSerializer(matches1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class lobbyList(APIView):

    def get(self, request):
        pass

    def post(self):
        pass
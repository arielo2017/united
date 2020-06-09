from rest_framework import  serializers
from . models import users
from . models import matchmaking
from . models import training
from . models import lobby


class usersSerializer(serializers.ModelSerializer):


    class Meta:
        model = users
        fields= '__all__'


class matchSerializer(serializers.ModelSerializer):

    class Meta:
        model = matchmaking
        fields= '__all__'


class trainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = training
        fields = ['user_id', 'City', 'form_name', 'Date']

class lobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = lobby
        fields= '__all__'


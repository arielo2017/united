from rest_framework import  serializers
from . models import users
from . models import matchmaking


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
        model = matchmaking
        fields= '__all__'

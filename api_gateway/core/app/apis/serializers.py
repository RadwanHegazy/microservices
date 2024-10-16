from rest_framework import serializers

class TodoSerializer (serializers.Serializer) : 
    text = serializers.CharField()

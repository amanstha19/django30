from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    address = serializers.CharField()
    email = serializers.EmailField()


from rest_framework import serializers
from home.models import Student, ClassRoom


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    address = serializers.CharField()
    email = serializers.EmailField()


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]

class StudentModelSerializer(serializers.ModelSerializer):
    # classroom = ClassRoomModelSerializer()
    class Meta:
        model = Student
        fields = ["id", "name", "email", "address", "classroom"]




    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower() == 'get':
            fields['classroom'] = ClassRoomModelSerializer()

        return fields
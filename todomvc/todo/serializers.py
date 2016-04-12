from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.Serializer):

    class Meta:
        model = Todo
        fields = '__all__'

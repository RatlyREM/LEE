from rest_framework import serializers
from .models import Routine
from .models import RoutineDetail

class RoutineSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = Routine.objects.create(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.routine_name = validated_data.get('routine_name', instance.routine_name)
        instance.routine_comment = validated_data.get('routine_comment', instance.routine_comment)
        instance.routine_day = validated_data.get('routine_day', instance.routine_day)
        instance.save()
        return instance

    class Meta:
        model = Routine
        #fields = ['routine_id', 'routine_name', 'routine_comment', 'recommend_count','routine_day', 'owner_id', 'created_at']
        fields = ['routine_name', 'routine_comment', 'routine_day', 'owner_id']
class RoutineDetaiSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = RoutineDetail.objects.create(**validated_data)
        return instance

   # def update(self):

    class Meta:
        model= RoutineDetail
        fields= ['__all__']
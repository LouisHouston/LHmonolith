from rest_framework import serializers
from .models.models import  User, FishingLog


        
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class FishingLogSerializer(serializers.ModelSerializer):
    fish_name = serializers.CharField(source='fish_id.name', read_only=True)
    bait_name = serializers.CharField(source='bait_id.name', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    caught_on = serializers.DateTimeField(format="%b %d, %Y %I:%M %p") 

    class Meta:
        model = FishingLog
        fields = ['catch_id', 'fish_id', 'fish_name', 'bait_id', 'bait_name', 'bow_id', 'user', 'username', 'caught_on']

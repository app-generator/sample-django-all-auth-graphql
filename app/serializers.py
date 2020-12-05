from rest_framework import serializers

from app.models import Traffic, Visit


class TrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

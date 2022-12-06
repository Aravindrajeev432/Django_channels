from rest_framework import serializers
from .models import Bay

class BaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Bay
        fields="__all__"
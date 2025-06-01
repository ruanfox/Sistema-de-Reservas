from rest_framework import serializers
from api.models.tables import Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
        
    def create(self, validated_data):
        table = Table(**validated_data)
        table.save()
        return table

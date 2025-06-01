from rest_framework import serializers
from api.models.users import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'senha': {'write_only': True}
        }

    def create(self, validated_data):
        senha = validated_data.pop('senha')
        user = User(**validated_data)
        user.set_password(senha)
        user.save()
        return user
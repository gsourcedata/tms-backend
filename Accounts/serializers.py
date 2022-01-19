from rest_framework import serializers

from .models import GsUser




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GsUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print("validated_data-------------------------------",validated_data )
        user = GsUser(
        email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    # def update(self, instance, validated_data):
    #     if 'user' in validated_data:
    #         instance.user.password = set_password(
    #             validated_data.get('user').get('password', instance.user.password)
    #         )
    #         instance.user.save()
from rest_framework import serializers
from .models import Client, ClientRequest, Seller, SellerProduct

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Client(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ClientRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('email', 'password')

    def create(self, validated_data):
        return Client.objects.create_user(**validated_data)


class ClientLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Seller(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ClientRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientRequest
        fields = ['request_id', 'client', 'min_price', 'max_price', 'request_date', 'end_date', 'product_type', 'product_details', 'key_words', 'product_con']
        read_only_fields = ['request_id', 'client', 'request_date']

class SellerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProduct
        fields = ['product_id', 'seller', 'image', 'key_words']
        read_only_fields = ['product_id']



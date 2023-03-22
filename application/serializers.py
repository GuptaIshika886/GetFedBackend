from rest_framework import serializers
from .models import RegisteredUsers
from .models import Canteen
from .models import Categories
from .models import ViewProfile
from .models import RegisteredCntnOwners

class RegisteredUsersSerializers(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    pwd=serializers.CharField(max_length=100)
    cpwd=serializers.CharField(max_length=100)

    def create(self,validate_data):
        print("Create Method Called")
        return RegisteredUsers.objects.create(**validate_data)
    
class RegisteredCntnOwnersSerializers(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    cname=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    pwd=serializers.CharField(max_length=100)
    cpwd=serializers.CharField(max_length=100)

    def create(self,validate_data):
        print("Create Method Called")
        return RegisteredCntnOwners.objects.create(**validate_data)    

class CanteenSerializers(serializers.Serializer):
    c_id=serializers.CharField(max_length=12)
    c_email=serializers.EmailField(max_length=100)
    c_name=serializers.CharField(max_length=100)
    c_address=serializers.CharField(max_length=100)
    c_phoneNo=serializers.CharField(max_length=10)
    c_feedback=serializers.IntegerField()

    def create(Self,validate_data):
        return Canteen.objects.create(**validate_data)

class CategoriesSerializers(serializers.Serializer):
    c_id=serializers.CharField(max_length=12)
    item_name=serializers.CharField(max_length=100)
    item_price=serializers.FloatField()

class ViewProfileSerializers(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)

    def create(self,validate_data):
        return ViewProfile.objects.create(**validate_data)
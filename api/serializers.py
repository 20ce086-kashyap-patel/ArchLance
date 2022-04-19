from rest_framework import serializers
from .models import ArchitectureAccount, ClientAccount, Project
from django.contrib.auth import get_user_model

User = get_user_model()


  
    
class UserSerializers(serializers.ModelSerializer):
    # user = ClientAccountSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            "password":{
                'write_only':True
            }
        }

    def create(self, validated_data):
        print(validated_data)
        user = super(UserSerializers, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # print(validated_data['user_role'])
        if validated_data['user_role'] == 'C':
            client_profile = ClientAccount.objects.create(
                user = user ,
                Username = validated_data['username'],
                Email = validated_data['email']
            )
        else:
            architecture_profile = ArchitectureAccount.objects.create(
                user = user ,
                Username = validated_data['username'],
                Email = validated_data['email']
            )
        return user

class ArchitectureAccountSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    class Meta:
        model = ArchitectureAccount
        fields = ['id','Name','Username','user','Number','Email','Profile_pic','Address','Reviews','city','date_time']
  


class ClientAccountSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    class Meta:
        model = ClientAccount
        fields = ['id','Name','Username','Number','Email','Profile_pic','city','date_time','user']


class ProjectSerializer(serializers.ModelSerializer):
    posted_by = ClientAccountSerializer(read_only=True)
    apply_for = ArchitectureAccountSerializer(read_only=True,many=True)
    class Meta:
        model = Project
        fields = ['id','name','posted_by','img','createdAt','desc','apply_for']
        
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseuserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','email','password','first_name','last_name']
        
class UserSerializer(BaseuserSerializer):
    class Meta(BaseuserSerializer.Meta):
        fields = ['id','username','email','first_name','last_name']
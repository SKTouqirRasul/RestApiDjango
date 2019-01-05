from rest_framework import serializers
from testapp.models import Status

class StatusSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source ='user.username')
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

    def validate_content(self,value):
        if len(value)>10000:
            raise serializers.ValueError('to many chareactes')
        return value

    def validate(self,data):
        content = data.get('content',None)
        if content == "":
            content=None
        image = data.get('image',None)
        if content == None and image == None:
            raise serializers.ValueError('content or image is required')
        return data

"""
data = {'content':"i love you",'user':1,'image':None}
data = {'content':"i love you",'user':1,'image':None}

"""

"""
class StatusSerializer(serializers.Serializer):
    content = serializers.CharField()
    image = serializers.ImageField()
    user = serializers.PrimaryKeyRelatedField()

    def create(self,validate_data):
        return Status.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.content = validate_data.get('content')
        instance.image = validate_data.get('content')
        instance.user = validate_data.get('user')
        instance.save()
        return instance
"""

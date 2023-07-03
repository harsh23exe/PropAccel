from rest_framework import serializers
from .models import  Post

#Acts as a bridge between models and views 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'content']

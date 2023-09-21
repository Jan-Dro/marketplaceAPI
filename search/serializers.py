from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Categories, Post

class CategoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'title', 'content', 'category')

    def field_validator(self, post_data):
        title = post_data.get('title')
        content = post_data.get('content')
        category = post_data.get('category')

        if category is None or content is None or title is None:
            raise serializers.ValidationError("Please fill in required fields: Title, Content, Category")
        
    def validate(self, data):
        self.field_validator(data)
        return data
    
    def create(self, validated_data):
        title = validated_data.get('title')
        content = validated_data.get('content')
        category = validated_data.get('category')

        validated_data['title'] = title.capitalize()
        post = Post.objects.create(title=title, content=content, category=category)

        return post


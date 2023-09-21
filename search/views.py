from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Categories, Post
from django.contrib.auth.models import User
from .serializers import CategoriesModelSerializer, PostModelSerializer

class AllCategories(APIView):

    def get(self, request, category_id_or_name=None):
        if category_id_or_name is None:
            categories = Categories.objects.all()
        else:
            try:
                category_id = int(category_id_or_name)
                categories = get_object_or_404(Categories, pk=category_id)
            except ValueError:
                categories = get_object_or_404(Categories, category=category_id_or_name)

        serializer = CategoriesModelSerializer(categories, many=not isinstance(categories, Categories))
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request):
        serializer = CategoriesModelSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, category_id_or_name):
        try:
            category_id = int(category_id_or_name)
            category = get_object_or_404(Categories, pk=category_id)
        except ValueError:
            category = get_object_or_404(Categories, category=category_id_or_name)

        serializer = CategoriesModelSerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, category_id_or_name):
        try:
            category_id = int(category_id_or_name)
            category = get_object_or_404(Categories, pk=category_id)
        except ValueError:
            category = get_object_or_404(Categories, category=category_id_or_name)

        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AllPost(APIView):
    def get(self, request, category_id_or_name=None, post_id=None):
        if category_id_or_name is not None and post_id is None:
            try:
                category_id = int(category_id_or_name)
                category = get_object_or_404(Categories, pk=category_id)
            except ValueError:
                category = get_object_or_404(Categories, category=category_id_or_name)
            posts = Post.objects.filter(category=category)
            serializer = PostModelSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        if category_id_or_name is None:
            posts = Post.objects.all()
        else:
            try:
                category_id = int(category_id_or_name)
                category = get_object_or_404(Categories, pk=category_id)
            except ValueError:
                category = get_object_or_404(Categories, category=category_id_or_name)
            posts = Post.objects.filter(category=category)

        if post_id == 'all':
            serializer = PostModelSerializer(posts, many=True)
        else:
            post = get_object_or_404(posts, pk=post_id)
            serializer = PostModelSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, category_id_or_name=None):
        serializer = PostModelSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, category_id_or_name=None, post_id=None):
            try:
                post = Post.objects.get(pk=post_id, category__pk=category_id_or_name)
            except Post.DoesNotExist:
                return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

            serializer = PostModelSerializer(post, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id_or_name=None, post_id=None):
        post =  get_object_or_404(Post, pk=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
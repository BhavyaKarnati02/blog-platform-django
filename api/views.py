from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from blog.models import Post

from .serializers import PostSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request):

    if request.method == 'GET':

        posts = Post.objects.all().order_by('-created_at')

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(
                author=request.user
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post_detail(request, post_id):

    try:

        post = Post.objects.get(id=post_id)

    except Post.DoesNotExist:

        return Response(
            {'error': 'Post not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.user != post.author:

        return Response(
            {'error': 'You are not allowed'},
            status=status.HTTP_403_FORBIDDEN
        )

    if request.method == 'GET':

        serializer = PostSerializer(post)

        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = PostSerializer(
            post,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':

        post.delete()

        return Response(
            {'message': 'Post deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
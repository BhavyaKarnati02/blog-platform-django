from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def api_home(request):

    posts = Post.objects.all()

    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)
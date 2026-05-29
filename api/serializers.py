from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):

    author = serializers.CharField(
        source='author.username',
        read_only=True
    )

    likes = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:

        model = Post

        fields = [
            'id',
            'title',
            'content',
            'author',
            'likes',
            'created_at',
        ]

    def get_likes(self, obj):

        return obj.likes.count()
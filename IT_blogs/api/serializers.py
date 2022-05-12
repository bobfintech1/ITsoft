from rest_framework import serializers

from IT_blogs.models import ItMainBlogs


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItMainBlogs
        fields ='__all__'

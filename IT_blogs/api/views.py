from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from IT_blogs.api.serializers import BlogsSerializer
from IT_blogs.models import ItMainBlogs


@api_view(['GET', 'POST'])
def blog_list(request):

    if request.method == 'GET':
        blogs = ItMainBlogs.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = ItMainBlogs.objects.get(pk=pk)
    except ItMainBlogs.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogsSerializer(snippet)
        return Response(serializer.data)
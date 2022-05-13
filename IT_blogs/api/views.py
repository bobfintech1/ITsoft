from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from IT_blogs.api.serializers import BlogsServiceSerializer, MainServiceSerializer, ITSerializers, \
    PartnersServiceSerializer
from IT_blogs.blogs.Partners import PartnersModels
from IT_blogs.blogs.about import ItAboutModels
from IT_blogs.blogs.service import HeaderServices, MainService


@api_view(['GET', 'POST'])
def blog_list(request):

    if request.method == 'GET':
        blogs = HeaderServices.objects.all()
        serializer = BlogsServiceSerializer(blogs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = HeaderServices.objects.get(pk=pk)
    except HeaderServices.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogsServiceSerializer(snippet)
        return Response(serializer.data)\



class AboutAPI(APIView):
    def get(self, request):
        it = MainService.object_all()
        serializer = MainServiceSerializer(it, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = MainServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            error = {'msg': 'Data has been created Successfully'}
            return Response(error)
        return Response({'msg': serializer.errors})


class ItMainList(GenericAPIView, ListModelMixin):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ITMainRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PartnersAPI(APIView):
    def get(self, request):
        it = PartnersModels.object_all()
        serializer = PartnersServiceSerializer(it, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PartnersServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            error = {'msg': 'Data has been created Successfully'}
            return Response(error)
        return Response({'msg': serializer.errors})


class ItPartnersList(GenericAPIView, ListModelMixin):
    queryset = PartnersModels.objects.all()
    serializer_class = PartnersServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ITPartnersRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = PartnersModels.objects.all()
    serializer_class = PartnersServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


#
# @api_view(['GET', 'POST'])
# def mobile_list(request):
#
#     if request.method == 'GET':
#         blogs = MobileService.objects.all()
#         serializer = MobileSerializer(blogs, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def mobile_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = MobileService.objects.get(pk=pk)
#     except MobileService.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = MobileSerializer(snippet)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'POST'])
# def site_list(request):
#
#     if request.method == 'GET':
#         blogs = SiteStructureService.objects.all()
#         serializer = SiteSerializer(blogs, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def site_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = SiteStructureService.objects.get(pk=pk)
#     except SiteStructureService.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SiteSerializer(snippet)
#         return Response(serializer.data)
#

class AboutAPI(APIView):
    def get(self, request):
        it = ItAboutModels.object_all()
        serializer = ITSerializers(it, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = ITSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            error = {'msg': 'Data has been created Successfully'}
            return Response(error)
        return Response({'msg': serializer.errors})


class ItAboutList(GenericAPIView, ListModelMixin):
        queryset = ItAboutModels.objects.all()
        serializer_class = ITSerializers

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)


class ITRetrieve(GenericAPIView, RetrieveModelMixin):
        queryset = ItAboutModels.objects.all()
        serializer_class = ITSerializers

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)



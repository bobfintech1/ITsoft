from rest_framework import serializers

from IT_blogs.blogs.Partners import PartnersModels
from IT_blogs.blogs.about import ItAboutModels
from IT_blogs.blogs.service import HeaderServices, MainService


class BlogsServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderServices
        fields ='__all__'


class MainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainService
        fields ='__all__'


class PartnersServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersModels
        fields ='__all__'

#
# class MobileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MobileService
#         fields ='__all__'
#
#
# class SiteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SiteStructureService
#         fields ='__all__'
#


class ITSerializers(serializers.ModelSerializer):

    class Meta:
        model = ItAboutModels
        fields ='__all__'


from django.contrib import admin

# Register your models here.
# from IT_blogs.models import ItMainBlogs

# admin.site.register(ItMainBlogs)
from IT_blogs.blogs.Partners import PartnersModels
from IT_blogs.blogs.about import ItAboutModels
from IT_blogs.blogs.service import HeaderServices, MainService
from IT_blogs.blogs.mainpage import *

admin.site.register(HeaderServices)
admin.site.register(MainService)
admin.site.register(ItAboutModels)
admin.site.register(PartnersModels)

# admin.site.register(MobileService)
# admin.site.register(SiteStructureService)
# admin.site.register(ItAboutModels)

#nur
admin.site.register(MainPageHeaderModel)
admin.site.register(MainPageAboutModel)
admin.site.register(MainPageServiceModel)
admin.site.register(MainPageNumbersModel)
admin.site.register(MainPageBlogModel)






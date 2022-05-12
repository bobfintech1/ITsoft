from django.urls import include, path
from rest_framework import routers
from IT_blogs.api.views import blog_list, blog_detail, ItAboutList, \
    ITRetrieve, ITMainRetrieve, ItMainList, ItPartnersList, ITPartnersRetrieve
#nur
from IT_blogs.api.views import *

app_name = 'IT_blogs'


urlpatterns = [
    path('header/', blog_list),
    path('header/<int:pk>/', blog_detail),
    path('main/', ItMainList.as_view()),
    path('main/<int:pk>/', ITMainRetrieve.as_view()),
    # path('mobile/', mobile_list),
    # path('mobile/<int:pk>/', mobile_detail),
    path('about/', ItAboutList.as_view()),
    path('about/<int:pk>/', ITRetrieve.as_view()),
    path('partners/', ItPartnersList.as_view()),
    path('partners/<int:pk>/', ITPartnersRetrieve.as_view()),
    #nur
    path('mainpage/header/', MainPageHeaderView.as_view()),
    path('mainpage/header/<int:pk>/', MainPageHeaderIdView.as_view()),
    path('mainpage/about/', MainPageAboutView.as_view()),
    path('mainpage/about/<int:pk>/', MainPageAboutIdView.as_view()),
    path('mainpage/service/', MainPageServiceView.as_view()),
    path('mainpage/service/<int:pk>/', MainPageServiceIdView.as_view()),
    path('mainpage/numbers/', MainPageNumbersView.as_view()),
    path('mainpage/numbers/<int:pk>/', MainPageNumbersIdView.as_view()),
    path('mainpage/blog/', MainPageBlogView.as_view()),
    path('mainpage/blog/<int:pk>/', MainPageBlogIdView.as_view()),






    




]


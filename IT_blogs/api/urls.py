from django.urls import include, path
from rest_framework import routers
from IT_blogs.api.views import blog_list, blog_detail, ItAboutList, \
    ITRetrieve, ITMainRetrieve, ItMainList, ItPartnersList, ITPartnersRetrieve

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

]


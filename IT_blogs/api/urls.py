from django.urls import include, path
from rest_framework import routers
from IT_blogs.api.views import blog_list, blog_detail

app_name = 'IT_blogs'

urlpatterns = [
    path('list/', blog_list),
    path('list/<int:pk>/', blog_detail)

]


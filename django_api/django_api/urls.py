"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from news_app import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'search_or', views.SearchOrViewSet, base_name='search_or')
router.register(r'search_and', views.SearchAndViewSet, base_name='search_and')
router.register(r'lookup_url', views.LookupUrlViewSet, base_name='lookup_url')
router.register(r'lookup_date', views.LookupDateViewSet, base_name='lookup_date')

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # url(r'^search/(?P<keywords>(\w|\s)*$)', views.get_all)
]

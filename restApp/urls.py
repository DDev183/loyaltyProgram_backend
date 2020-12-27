"""restApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from restApp.quickstart import views
# from restApp.quickstart.views import RegistrationAPIView
# from restApp.quickstart.views import LoginAPIView



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    # re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    # path to djoser end points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # path to our account's app endpoints
    path("api/accounts/", include("restApp.quickstart.urls")),
    # gets all user profiles and create a new profile
    path("all-profiles", views.UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", views.userProfileDetailView.as_view(), name="profile"),
    # path('user/', views.user),
    path('spi/', views.snippet_list),
    path('log/', views.log),
    path('card/', views.card),
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

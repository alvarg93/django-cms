"""badura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from rest_framework import routers

from app import views as store

router = routers.DefaultRouter()
router.register(r'users', store.UserViewSet)
router.register(r'users', store.GroupViewSet)
router.register((r'books'), store.BookViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url('', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', store.index, name="index"),
    url(r'^test/(?P<text>\w{0,50})/?$', store.test, name="test", ),
    url(r'^books/', store.books, name="books"),
    url(r'^booksAngular/', store.booksAngular, name="books"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

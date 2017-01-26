from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url('', include('registration.backends.default.urls'), name="auth"),
    url('', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^posts/$', views.posts, name="posts"),
    url(r'^authors/$', views.authors, name="authors"),
    url(r'^posts/([0-9]+)/$', views.post, name="post"),
    url(r'^authors/([0-9]+)/$', views.author, name="author"),
    url(r'^test/(?P<text>\w{0,50})/?$', views.test, name="test", ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

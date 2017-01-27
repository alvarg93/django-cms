from django.conf.urls import url, include
from django.contrib import admin

from app import views

urlpatterns = [
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

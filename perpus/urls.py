"""perpus URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from mainapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^listbook/$', views.listbook, name='listbook'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    url(r'^addrental/$', views.addrental, name='addrental'),
    url(r'^listrental/$', views.listrental, name='listrental'),
    url(r'^completerental/(?P<id>[0-9]+)/$', views.completedrental, name='completed'),
    url(r'^editbook/(?P<id>[0-9]+)/$', views.editbook, name='editbook'),
    url(r'^detailbook/(?P<id>[0-9]+)/$', views.detailbook, name='detailbook'),
    url(r'^deletebook/(?P<id>[0-9]+)/$', views.deletebook, name='deletebook'),
    url(r'^listuser/$', views.listuser, name='listuser'),
    url(r'^edituser/(?P<id>[0-9]+)/$', views.edituser, name='edituser'),
    url(r'^detailuser/(?P<id>[0-9]+)/$', views.detailuser, name='detailuser'),
    url(r'^hapususer/(?P<id>[0-9]+)/$', views.deleteuser, name='hapususer'),
    url(r'^regisuser/$', views.adduser, name='adduser')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

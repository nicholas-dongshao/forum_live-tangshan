"""tangshanren URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

import spirit.urls
import live.urls
import mine.urls
import live_support.urls
import vircurrency.urls
import adconfig.urls
import updateApp.urls

# Override admin login for security purposes
from django.contrib.auth.decorators import login_required
admin.site.login = login_required(admin.site.login)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(spirit.urls)),
    url(r'^live/', include(live.urls)),
    url(r'^mine/', include(mine.urls)),
    url(r'^support/', include(live_support.urls)),
    url(r'^vircurrency/', include(vircurrency.urls)),
    url(r'^adconfig/', include(adconfig.urls)),
    url(r'^update/', include(updateApp.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

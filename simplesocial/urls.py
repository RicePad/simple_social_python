"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url  # For django versions before 2.0
from django.contrib import admin
from simplesocial import views
from simplesocial.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r"^test/$", views.TestView.as_view(), name=LOGIN_REDIRECT_URL),
    url(r"^thanks/$", views.ThanksView.as_view(), name=LOGOUT_REDIRECT_URL),
    url(r'^accounts/', include("accounts.urls", namespace="accounts")),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^posts/", include("posts.urls", namespace="posts")),
    url(r"^groups/",include("groups.urls", namespace="groups")),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
         url(r'^__debug__/', include(debug_toolbar.urls)),

        

    ] + urlpatterns

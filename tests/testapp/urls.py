from django.conf.urls import url, include
from django.contrib import admin
from testapp.views import PathIsTemplateNameQueryStringContextView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^(?P<template_name>.*)$',
        PathIsTemplateNameQueryStringContextView.as_view()),
]

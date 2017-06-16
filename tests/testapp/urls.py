from django.conf.urls import url, include
from django.contrib import admin
from testapp.views import PathIsTemplateNameQueryStringContextView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls), {}, "admin-index"),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^(?P<template_name>.*)$',
        PathIsTemplateNameQueryStringContextView.as_view()),
]

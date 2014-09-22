from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # any url ending in books with point to books->views->index
    # In Books folder edit views.py
    url(r'^books/$', 'books.views.index')
)

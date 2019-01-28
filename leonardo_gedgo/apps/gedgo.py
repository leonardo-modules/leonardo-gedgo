from __future__ import absolute_import

from django.conf.urls import url
from django.shortcuts import redirect

from gedgo import views

urlpatterns = [
    url(
        r'^(?P<gedcom_id>\d+)/(?P<person_id>I\d+)/$',
        views.person,
        name='person'
    ),
    url(r'^(?P<gedcom_id>\d+)/$', views.gedcom, name='gedcom'),

    # XHR Data views
    url(r'^(?P<gid>\d+)/pedigree/(?P<pid>I\d+)/$', views.pedigree),
    url(r'^(?P<gid>\d+)/timeline/(?P<pid>I\d+)/$', views.timeline),
    # url(r'^dashboard/worker/status$', views.worker_status),

    url(r'^blog/$', views.blog_list),
    url(r'^blog/(?P<year>\d+)/(?P<month>\d+)/$', views.blog),
    url(r'^blog/post/(?P<post_id>\d+)/$', views.blogpost),
    url(r'^documentaries/$', views.documentaries),
    url(r'^documentaries/(?P<title>.+)/$', views.documentary_by_id),
    url(r'^document/(?P<doc_id>\w+)/$', views.document),
    # url(r'^research/(?P<pathname>.*)$', views.research),
    url(r'^search/$', views.search, name='gedgo_search'),
    # url(r'^dashboard/$', views.dashboard),
    # url(r'^dashboard/user/(?P<user_id>\d+)/$', views.user_tracking),

    url(r'^$', lambda r: redirect('/gedgo/1/')),
]

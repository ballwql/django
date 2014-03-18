
from django.conf.urls import patterns, include, url
from bookmarks.views import *
from bookmarks.feeds import *
from django.views.generic import TemplateView
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',                       
#                       url(r'^polls/',include('polls.urls')),
#                       url(r'^polls/',include('polls.urls',namespace="polls")),# namespacing urls names
                       #admin management
                       url(r'^admin/', include(admin.site.urls)),
					   url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
                       #comments
                       url(r'^comments/',include('django.contrib.comments.urls')),
                       
                       #Feeds
                       url(r'^feeds/(?P<url>.*)/$',RecentBookmark()),
                       #Friends
                       url(r'^friends/(\w+)/$',friend_page),
                       url(r'^friend/add/$',friend_add),
                       #Browsing
                       url(r'^$',main_page),
                       url(r'^popular/$',popular_page),
                       url(r'^user/(\w+)/$',user_page),
                       #session management
                       url(r'^login/$','django.contrib.auth.views.login'),
                       url(r'^logout/$',logout_page),
                       url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
                       url(r'^register/$',register_page),
                       url(r'^register/success/$',TemplateView.as_view(template_name='registration/register_success.html')),
                       #Account management
                       url(r'^save/$',bookmark_save_page),
                       url(r'^tag/([^\s]+)/$',tag_page),
                       url(r'^tag/$',tag_cloud_page),
                       url(r'^search/$',search_page),
                       url(r'^vote/$',bookmark_vote_page),
                       url(r'^bookmark/(\d+)/$',bookmark_page),
					   #Depot app
					   url(r'^depot/',include('depot.urls')),
					   #DBRelease app
					   url(r'^dbrelease_app/',include('dbrelease_app.urls')),
                       )

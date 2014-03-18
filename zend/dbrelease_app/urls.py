
from django.conf.urls import *
from models import *
from views import *

urlpatterns = patterns('',
    url(r'accounts/login/$', login),  
    url(r'accounts/logout/$',logout),
	url(r'accounts/changepwd/$',changepwd),
	url(r'accounts/createtask/$',createtask),
	url(r'accounts/tasklist/$',tasklist),
)

from django.conf.urls.defaults import *

urlpatterns = patterns('index.views',
    url(r'^$', 'index', name='index'),
    url(r'^check_db/$', 'check_db', name='index_check_db'),
    url(r'check_store/$', 'check_store', name='index_check_store'),
    url(r'sales/$', 'sales', name='index_sales'),
)
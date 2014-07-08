from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from lintel.views import draw_graph
from lintel.views import barchart
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linteltest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^goc/(?P<comp_name>[a-zA-Z0-9_.-]+)/(?P<date>[0-9]+)/$','lintel.views.get_data'),
    url(r'^goc_range/(?P<comp_name>[a-zA-Z0-9_.-]+)/(?P<start_date>[0-9]+)/(?P<end_date>[0-9]+)$','lintel.views.get_alldata'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','lintel.views.home'),
    url(r'^graph/', draw_graph),
    url(r'^charts/bar/$', 'barchart'),
)

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'reserve'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^browse$', views.browse, name='browse'),
    url(r'^space/(?P<space_id>[0-9]+)/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$', views.space_details, name='space'),
    url(r'^myaccount/(?P<user_id>[0-9]+)/$', views.account, name='my_account'),
    url(r'^edit_myaccount/(?P<user_id>[0-9]+)/$', views.account, name='my_account'),
    url(r'^myreservations/(?P<user_id>[0-9]+)/$', views.reservation, name='reservation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import url 
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about/$',views.about, name='about'),
    url(r'^post/$', views.post, name='post'),
    url(r'^post/new', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail),
    url(r'^(?P<pk>\d+)/comments/new/$', views.comment_new),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^home/', views.home, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

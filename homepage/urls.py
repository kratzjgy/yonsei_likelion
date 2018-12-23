from django.conf.urls import url 
from . import views
  
urlpatterns = [
<<<<<<<HEAD
    url(r'^$',views.index,name = 'index.html'),
=======
    url(r'^$', views.index, name='index'),
    url(r'^about/',views.about, name='about'),
>>>>>>> d56dfe54ac1b9cf803986ad5fec8dc620437e78c
]
from . import views
from django.conf.urls import url,include


urlpatterns = [
	url(r'^home/$',views.home,name='home'),
	url(r'^search/$',views.search,name='search'),
]
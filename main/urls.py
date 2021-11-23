from django.conf.urls import url, include
from main import views




# Template Tagging 
app_name="main"

urlpatterns = [
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^services/$', views.services, name='services'),
	url(r'^sidebar_right/$', views.sidebar_right, name='sidebar_right'),
	url(r'^projects/$', views.projects, name='projects'),
	url(r'^prices/$', views.prices, name='prices'),

]
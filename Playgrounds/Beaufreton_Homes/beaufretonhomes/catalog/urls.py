from django.urls import path, re_path

from . import views

urlpatterns = [
	# The main mage (first page)
	path('', views.index, name='index'),

	# The detail page (second page)
	path('home-details/', views.details, name="home-details"),
	re_path(r'^home-details/(?P<start_date>\d+)/(?P<end_date>\d+)$', views.details, name="home-details"),

	# The booking page (third page)
	path('booking/', views.booking, name="booking"),
	re_path(r'^booking/(?P<start_date>\d+)/(?P<end_date>\d+)$', views.booking, name="booking"),
]
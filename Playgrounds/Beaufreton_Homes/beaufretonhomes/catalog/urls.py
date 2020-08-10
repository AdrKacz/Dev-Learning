from django.urls import path

from . import views

urlpatterns = [
	# The main mage (first page)
	path('', views.index, name='index'),

	# The detail page (second page)
	path('home-details/', views.details, name="home-details"),

	# The booking page (third page)
	path('booking/', views.booking, name="booking"),
]
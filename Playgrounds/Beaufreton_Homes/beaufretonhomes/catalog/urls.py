from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('home-details', views.details, name="home-details"),
	# path('logement/<int:pk>', views.LogementDetailView.as_view(), name='logement-detail'),
]
from django.shortcuts import render

# Create your views here.

from .models import Logement, Reservation, Photographie

def index(request):
	"""View function for home page of site."""

	# Get one image to put as background

	# Do not retreive "image" to save memory
	# Only take those who can be put on background
	# Shuffle and take the first one
	background_image = Photographie.objects.defer('image').filter(page_principale__exact=True).order_by('?')[0]

	# Get the other image for the gallery
	all_images = Photographie.objects.all()

	# Render the HTML template index.html with the data in the context variable.

	return render(
		request,
		'index.html',
		context={'background': background_image, 'all_images': all_images},
		)
	
from django.views import generic

# class LogementDetailView(generic.DetailView):
# 	"""Generic class-based detail view for a Logement."""
# 	model = Logement

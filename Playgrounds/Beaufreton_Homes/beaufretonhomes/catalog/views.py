from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# To handle forms
from catalog.forms import PickDatesForm

# Create your views here.

from .models import Logement, Reservation, Photographie, Caracteristique

def index(request):
	"""View function for home page of site.
	Handle a form in its core.
	"""
	# Get one image to put as background

	# Do not retreive "image" to save memory
	# Only take those who can be put on background
	# Shuffle and take the first one
	background_image = Photographie.objects.filter(page_principale__exact=True).order_by('?')[0]

	# Get the other image for the gallery
	all_images = Photographie.objects.all().order_by('?')[:10]

	# [DEBUG ONLY] Create more image from one
	if all_images.count() < 10:
		all_images = [image[0] for image in list(all_images.values_list('image'))] * 5
		all_images = all_images[:10]

	

	# Get the "caracteristique"
	characteristics = Caracteristique.objects.all().order_by("z_axis")[:8]

	# Create the context
	context = {
	'background': background_image, 
	'all_images': all_images,
	'characteristics': characteristics}

	# Handle the form (date choices)

	# If this is a POST request then process the Form data
	if request.method == 'POST':
		# Create a form instance and populate it with the data from the request (binding)
		form = PickDatesForm(request.POST)
		context['form'] = form

		# Check if the form is valid
		if form.is_valid():
			# Process the data in form.cleaned_data as required
			return HttpResponseRedirect(reverse('home-details'))

	# If this is a GET (or any other method) create the default form
	else:
		form = PickDatesForm(initial={'start_date': '', 'end_date': ''})
		context['form'] = form


	# Render the HTML template index.html with the data in the context variable.
	print("Context:", context)
	return render(
		request,
		'index.html',
		context=context,
		)

def details(request):
	"""View function for second page of the site.
	Home details and second date selection.
	"""
	#home_images = Photographie.objects.filter(logement)


	return render(
		request,
		'home-details.html',)
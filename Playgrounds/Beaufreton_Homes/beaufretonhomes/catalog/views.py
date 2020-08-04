from django.shortcuts import render

# Create your views here.

from .models import Logement, Reservation

def index(request):
	"""View function for home page of site."""

	# Generate counts of some of the main objects
	num_logement = Logement.objects.all().count()

	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	# Render the HTML template index.html with the data in the context variable.

	return render(
		request,
		'index.html',
		context={'num_logement': num_logement, 'num_visits': num_visits},
		)


from django.views import generic

class LogementListView(generic.ListView):
	"""Generic class-based view for a list of Logements."""
	model = Logement

class LogementDetailView(generic.DetailView):
	"""Generic class-based detail view for a Logement."""
	model = Logement


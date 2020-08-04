from django.db import models

# Create your models here.

from django.urls import reverse # To generate ULRs by reversing URL patterns

import uuid # Required for unique book instances

from datetime import date

class Logement(models.Model):
	"""Model representing a "Logement" """

	nom = models.CharField(
		null=True,
		max_length=200,
		help_text="Entre le nom du logement")

	capacite = models.IntegerField(
		default=0,
		help_text="Entre la capacité maximum du logement")

	class Meta:
		ordering = ['nom']

	def get_absolute_url(self):
		"""Returns the url to access a particular "logement" instance"""
		return reverse('logement-detail', args=[str(self.id)])

	def __str__(self):
		return self.nom

class Reservation(models.Model):
	"""Model representing one transaction i.e. "reservation" """

	logement = models.ForeignKey(
		'Logement',
		on_delete=models.CASCADE,
		null=True,
		blank=True)

	debut = models.DateField(
		null=True,
		blank=True)

	fin = models.DateField(
		null=True,
		blank=True)

	class Meta:
		ordering = ['debut', 'fin']

	def __str__(self):
		return f'{self.logement.nom} ({self.debut} - {self.fin})'




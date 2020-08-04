from django.contrib import admin

# Register your models here.

from .models import Logement, Reservation


""" Minimal registrations of Models.
admin.site.register(Logement)
admin.site.register(Reservation)
"""


class ReservationsInline(admin.TabularInline):
	"""Defines format of inline reservation insertion (used in LogementAdmin)"""
	model = Reservation
	extra = 0

@admin.register(Logement)
class LogementAdmin(admin.ModelAdmin):
	"""Administration object for Logement models.
	Defines:
		- 	fields to be displayed in list view (list_display)
		- 	adds inline addition of Reservation instances in Logement view (inlines)
	"""

	list_display = ('nom', 'capacite')
	inlines = [ReservationsInline]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	"""Administration object for Reservation models.
	Defines:
		- 	fields to be displayed in list view (list_display)
		-	filters that will be displayed in sidebar (list_filter)
		- 	grouping of fields into sections (fieldsets)
	"""

	list_display = ('logement', 'debut', 'fin')
	list_filter = ('logement', 'debut', 'fin')

	fieldsets = (
		(None, {
			'fields': ('logement',)
		}),
		('Dates', {
			'fields': ('debut', 'fin')
		}),
	)
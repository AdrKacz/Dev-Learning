from django.contrib import admin

# Register your models here.

from .models import Logement, Reservation, Photographie, Caracteristique, Option


""" Minimal registrations of Model exemple
admin.site.register(Logement)
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

	list_display = ('nom', 'prix', 'capacite')
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

@admin.register(Photographie)
class PhotographieAdmin(admin.ModelAdmin):
	"""Administration object for Caracteristique models.
	Defines:
		- 	fields to be displayed in list view (list_display)
		-	filters that will be displayed in sidebar (list_filter)
	"""

	list_display = ('nom', 'logement', 'page_principale')
	list_filter = ('logement', 'page_principale')

@admin.register(Caracteristique)
class CaracteristiqueAdmin(admin.ModelAdmin):
	"""Administration object for Caracteristique models.
	Defines:
		- 	fields to be displayed in list view (list_display)
		-	filters that will be displayed in sidebar (list_filter)
	"""

	list_display = ('description', 'icon', 'z_axis')
	list_filter = ('z_axis',)

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
	"""Administration object for Caracteristique models.
	Defines:
		- 	fields to be displayed in list view (list_display)
		-	filters that will be displayed in sidebar (list_filter)
	"""

	list_display = ('nom', 'prix', 'plusieurs')
	list_filter = ('prix', 'plusieurs')
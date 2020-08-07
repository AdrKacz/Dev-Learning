# Forms Handling
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import datetime


class PickDatesForm(forms.Form):
	start_date = forms.DateField(
		help_text="Arrivée",
		required=True,
		widget=forms.TextInput(attrs={
			"value": "Arrivée"}))

	end_date = forms.DateField(
		help_text="Départ",
		required=True,
		widget=forms.TextInput(attrs={
			"value": "Départ"}))

	def clean_start_date(self):
		data = self.cleaned_data['start_date']

		# Check if the date is not in the past
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - start date in the past'))

		return data

	def clean_end_date(self):
		data = self.cleaned_data['end_date']

		# Check if the date is not in the past
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - end date in the past'))

		return data

	def clean(self):
		cleaned_data = super().clean()
		data_start = cleaned_data.get("start_date")
		data_end = cleaned_data.get("end_date")

		print("Data:", data_start, data_end)

		if data_start and data_end:
			if data_end <= data_start:
				raise ValidationError(_('Invalid date - end date before start date'))
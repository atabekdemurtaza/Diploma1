from django import forms 
from quotes.models import Quote
from django.forms import ModelForm

class QuoteForm(ModelForm):

	required_css_class = 'required'
	class Meta:

		model = Quote 
		fields = '__all__'


from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from people.models import Person

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('name', 'address', 'dob', 'phone')
		name = forms.CharField(max_length=150)
		address = forms.CharField(max_length=200, widget=forms.Textarea)
		dob = forms.DateField(input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'])
		phone = forms.CharField(max_length=30)

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    self.helper = FormHelper()
	    self.helper.form_method = 'post'
	    self.helper.add_input(Submit('submit', 'Save'))	
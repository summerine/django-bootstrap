from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Person
from people.forms import PersonForm

# Create your views here.
class PersonListView(ListView):
	model = Person
	context_object_name = 'people'

class PersonCreateView(CreateView):
	model = Person
	fields = ('name', 'address', 'dob', 'phone')
	success_url = reverse_lazy('person_list')

class PersonUpdateView(UpdateView):
	model = Person
	form_class = PersonForm
	template_name = 'people/person_update_form.html'	
	success_url = reverse_lazy('person_list')

class PersonDeleteView(DeleteView):
	model = Person
	template_name = 'people/person_confirm_delete.html'
	success_url = reverse_lazy('person_list')	

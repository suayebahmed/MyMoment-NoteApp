from django.shortcuts import render
from .models import Moment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import MomentForm
from django.urls import reverse_lazy


# home page view: All the moments will show as a list item (date, title)
class HomePageView(ListView):
    model = Moment
    template_name = 'home.html'
    ordering = ['-id']

# Each moment in a single page (date, title, text)
class MomentDetailView(DetailView):
    model = Moment
    template_name = 'moment_detail.html'

# Create New Moment
class AddMomentView(CreateView):
    model = Moment
    form_class = MomentForm
    template_name = 'add_moment.html'
    # fields = '__all__'
    # fields = ('title', 'date', 'text')

# Update Any Moment
class EditMomentView(UpdateView):
    model = Moment
    form_class = MomentForm
    template_name = 'edit_moment.html'
    # fields = '__all__'


class DeleteMomentView(DeleteView):
    model = Moment
    template_name = 'delete_moment.html'
    success_url = reverse_lazy('home-page')
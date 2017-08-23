from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Day, Time, Program


class DayDetailView(DetailView):
	model = Day
	slug_field = 'name'
	slug_url_kwarg = 'day'

	def get_context_data(self, **kwargs):
		context = super(DayDetailView, self).get_context_data(**kwargs)
		this_day = Day.objects.all().filter(name=self.kwargs['day']).first().id
		context['time_list'] = Time.objects.all().filter(day=this_day).order_by('start')
		context['today_programs'] = Program.objects.all()
		return context

class DayListView(ListView):
	model = Day

class ProgramListView(ListView):
	model = Program


class ProgramDetailView(DetailView):
	model = Program

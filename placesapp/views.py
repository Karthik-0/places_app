from django.views import generic
from .models import Place
from . import forms


class PlaceList(generic.ListView):
    template_name = 'index.html'
    model = Place
    context_object_name = 'places'


class PlaceDetail(generic.DetailView):
    template_name = 'detail.html'
    model = Place
    context_object_name = 'place'

    def get_object(self, queryset=None):
        obj = super(PlaceDetail, self).get_object(queryset=queryset)
        print(obj.location.coords)
        return obj


class PlaceCreate(generic.CreateView):
    template_name = 'add.html'
    model = Place
    success_url = '/places'
    # fields = ['title','desc','location']
    form_class = forms.PlaceForm

from django.views import generic
from .models import Place


class PlaceList(generic.ListView):
    template_name = 'index.html'
    model = Place
    context_object_name = 'places'

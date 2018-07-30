from django.views import generic
from .models import Place


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

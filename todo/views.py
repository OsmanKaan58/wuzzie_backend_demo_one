from django.views.generic import ListView
from .models import Monster


class AllMonsters(ListView):
    model = Monster
    template_name = "templates/index.html"


class OldMOnsters(ListView):
    model = Monster
    template_name = "templates/old.html"

    def get_queryset(self):
        return Monster.objects.filter(age=7)

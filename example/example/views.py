from django.views.generic import CreateView, ListView, UpdateView

from .forms import ExampleForm
from .models import Record


class ExampleView(CreateView, ListView):
    template_name = "example/form.html"
    success_url = "/"
    model = Record
    form_class = ExampleForm
    object_list = Record.objects.all()


class ExampleUpdateView(UpdateView):
    template_name = "example/form.html"
    success_url = "/"
    model = Record
    form_class = ExampleForm
    object_list = Record.objects.all()

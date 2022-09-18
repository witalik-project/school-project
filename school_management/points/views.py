from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Classes
from .forms import ClassesEditCreateForm


class Index(ListView):
    template_name = "index.html"
    model = Classes
    context_object_name = "classes"


class CreateClass(CreateView):
    template_name = "create_class.html"
    model = Classes
    form_class = ClassesEditCreateForm
    success_url = "/"


class EditClass(UpdateView):
    template_name = "edit_class.html"
    model = Classes
    form_class = ClassesEditCreateForm
    success_url = "/"


class DeleteClass(DeleteView):
    template_name = "delete_class.html"
    model = Classes
    success_url = "/"

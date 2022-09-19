from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Classes, PointsLog
from .forms import ClassesEditCreateForm, PointsLogCreateEditForm


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


def create_points_log(request):
    if request.method == "POST":
        form = PointsLogCreateEditForm(request.POST)
        if form.is_valid():
            log = PointsLog(
                points_log_class=form.cleaned_data["points_log_class"],
                points_log_type=form.cleaned_data["points_log_type"],
                points_log_amount=form.cleaned_data["points_log_amount"]
            )
            if log.points_log_type == "+":
                log.points_log_class.class_points = log.points_log_class.class_points + log.points_log_amount
                log.points_log_class.save()
                log.save()
                return HttpResponseRedirect("/")
            elif log.points_log_type == "-":
                log.points_log_class.class_points = log.points_log_class.class_points - log.points_log_amount
                log.points_log_class.save()
                log.save()
                return HttpResponseRedirect("/")
    else:
        form = PointsLogCreateEditForm()

    return render(request, "create_points_log.html", {
        "form": form
    })


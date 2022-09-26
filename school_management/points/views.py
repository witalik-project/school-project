from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Classes, PointsLog, AddPointsLog, SubtractPointsLog
from .forms import ClassesEditCreateForm, PointsLogCreateEditForm, AddPointsLogCreateEditForm, \
    SubtractPointsLogCreateEditForm


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
        "form": form,
    })


def create_add_points_log(request, pk):
    points_add_log_class = get_object_or_404(Classes, pk=pk)
    if request.method == "POST":
        form = AddPointsLogCreateEditForm(request.POST)
        if form.is_valid():
            log = AddPointsLog(
                points_add_log_class=points_add_log_class,
                points_add_log_amount=form.cleaned_data["points_add_log_amount"]
            )
            log.points_add_log_class.class_points = log.points_add_log_class.class_points + log.points_add_log_amount
            log.points_add_log_class.save()
            log.save()
            return HttpResponseRedirect("/")
    else:
        form = AddPointsLogCreateEditForm()

    return render(request, "create_add_points_log.html", {
        "form": form,
        "classes": points_add_log_class
    })


def create_subtract_points_log(request, pk):
    points_subtract_log_class = get_object_or_404(Classes, pk=pk)
    if request.method == "POST":
        form = SubtractPointsLogCreateEditForm(request.POST)
        if form.is_valid():
            log = SubtractPointsLog(
                points_subtract_log_class=points_subtract_log_class,
                points_subtract_log_amount=form.cleaned_data["points_subtract_log_amount"]
            )
            log.points_subtract_log_class.class_points = log.points_subtract_log_class.class_points - log.points_subtract_log_amount
            log.points_subtract_log_class.save()
            log.save()
            return HttpResponseRedirect("/")
    else:
        form = SubtractPointsLogCreateEditForm()

    return render(request, "create_subtract_points_log.html", {
        "form": form,
        "classes": points_subtract_log_class
    })


def scoreboard(request):
    all_classes = Classes.objects.all().order_by("-class_points")

    return render(request, "scoreboard.html", {
        "classes": all_classes,
    })

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Classes, PointsLog
from .forms import ClassesEditCreateForm, ClassesEditExceptPointsForm, PointsLogCreateEditForm, \
    PointsAddSubtractLogCreateEditForm
from .filters import PointsLogFilter


class Index(ListView):
    template_name = "index.html"
    model = Classes
    context_object_name = "classes"


class Scoreboard(ListView):
    template_name = "scoreboard.html"
    model = Classes
    context_object_name = "classes"

    ordering = ['-class_points']


class LogsList(ListView):
    template_name = "logs.html"
    model = PointsLog
    context_object_name = "logs"

    ordering = ['-points_log_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PointsLogFilter(self.request.GET, queryset=self.get_queryset())
        return context


class CreateClass(LoginRequiredMixin, CreateView):
    template_name = "create_class.html"
    model = Classes
    form_class = ClassesEditCreateForm
    success_url = "/"


class EditClass(LoginRequiredMixin, UpdateView):
    template_name = "edit_class.html"
    model = Classes
    form_class = ClassesEditExceptPointsForm
    success_url = "/"


class DeleteClass(LoginRequiredMixin, DeleteView):
    template_name = "delete_class.html"
    model = Classes
    success_url = "/"


@login_required
def create_points_log(request):
    if request.method == "POST":
        form = PointsLogCreateEditForm(request.POST)
        if form.is_valid():
            log = PointsLog(
                points_log_class=form.cleaned_data["points_log_class"],
                points_log_type=form.cleaned_data["points_log_type"],
                points_log_amount=form.cleaned_data["points_log_amount"],
                points_log_created_by=request.user
            )
            if log.points_log_type:
                check_plus = log.points_log_class.class_points + log.points_log_amount
                if check_plus > 1000:
                    messages.add_message(request, messages.ERROR,
                                         f'You cannot add this amount of points. Now {log.points_log_class.class_number}{log.points_log_class.class_letter} class have: {log.points_log_class.class_points}/1000 points.')
                else:
                    log.points_log_class.class_points = log.points_log_class.class_points + log.points_log_amount
                    log.points_log_class.save()
                    log.save()
                    return HttpResponseRedirect("/")
            else:
                check_minus = log.points_log_class.class_points - log.points_log_amount
                if check_minus < 0:
                    messages.add_message(request, messages.ERROR,
                                         f'You cannot subtract this amount of points. Now {log.points_log_class.class_number}{log.points_log_class.class_letter} class have: {log.points_log_class.class_points}/1000 points. Cannot be under 0.')
                else:
                    log.points_log_class.class_points = log.points_log_class.class_points - log.points_log_amount
                    log.points_log_class.save()
                    log.save()
                    return HttpResponseRedirect("/")
    else:
        form = PointsLogCreateEditForm()

    return render(request, "create_points_log.html", {
        "form": form,
    })


@login_required
def add_points_log(request, pk):
    points_log_class = get_object_or_404(Classes, pk=pk)
    if request.method == "POST":
        form = PointsAddSubtractLogCreateEditForm(request.POST)
        if form.is_valid():
            log = PointsLog(
                points_log_class=points_log_class,
                points_log_type=True,
                points_log_amount=form.cleaned_data["points_log_amount"],
                points_log_created_by=request.user
            )
            check = log.points_log_class.class_points + log.points_log_amount
            if check > 1000:
                messages.add_message(request, messages.ERROR,
                                     f'You cannot add this amount of points. Now {points_log_class.class_number}{points_log_class.class_letter} class have: {points_log_class.class_points}/1000 points.')
            else:
                log.points_log_class.class_points = log.points_log_class.class_points + log.points_log_amount
                log.points_log_class.save()
                log.save()
                return HttpResponseRedirect("/")
    else:
        form = PointsAddSubtractLogCreateEditForm()

    return render(request, "create_add_points_log.html", {
        "form": form,
        "classes": points_log_class
    })


@login_required
def subtract_points_log(request, pk):
    points_log_class = get_object_or_404(Classes, pk=pk)
    if request.method == "POST":
        form = PointsAddSubtractLogCreateEditForm(request.POST)
        if form.is_valid():
            log = PointsLog(
                points_log_class=points_log_class,
                points_log_type=False,
                points_log_amount=form.cleaned_data["points_log_amount"],
                points_log_created_by=request.user
            )
            check = log.points_log_class.class_points - log.points_log_amount
            if check < 0:
                messages.add_message(request, messages.ERROR,
                                     f'You cannot subtract this amount of points. Now {points_log_class.class_number}{points_log_class.class_letter} class have: {points_log_class.class_points}/1000 points. Cannot be under 0.')
            else:
                log.points_log_class.class_points = log.points_log_class.class_points - log.points_log_amount
                log.points_log_class.save()
                log.save()
                return HttpResponseRedirect("/")
    else:
        form = PointsAddSubtractLogCreateEditForm()

    return render(request, "create_subtract_points_log.html", {
        "form": form,
        "classes": points_log_class
    })


def scoreboard(request):
    all_classes = Classes.objects.all().order_by("-class_points")
    return render(request, "scoreboard.html", {
        "classes": all_classes,
    })


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.add_message(request, messages.INFO, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.add_message(request, messages.ERROR, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_request(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request=request, template_name="logout.html")

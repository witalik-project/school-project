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


def create_classes(request):
    if request.method == "POST":
        create_classes.classes_form = ClassesEditCreateForm(request.POST)
        if create_classes.classes_form.is_valid():
            classes = Classes(
                class_number=create_classes.classes_form.cleaned_data["class_number"],
                class_letter=create_classes.classes_form.cleaned_data["class_letter"],
                class_school_level=create_classes.classes_form.cleaned_data["class_school_level"],
                class_teacher_name=create_classes.classes_form.cleaned_data["class_teacher_name"],
                class_teacher_surname=create_classes.classes_form.cleaned_data["class_teacher_surname"],
                class_points=create_classes.classes_form.cleaned_data["class_points"],
                class_photo=create_classes.classes_form.cleaned_data["class_photo"],
            )
            classes.save()
            return HttpResponseRedirect("/")
    else:
        create_classes.classes_form = ClassesEditCreateForm()


def create_points_log(request):
    if request.method == "POST":
        create_points_log.points_log_form = PointsLogCreateEditForm(request.POST)
        if create_points_log.points_log_form.is_valid():
            log = PointsLog(
                points_log_class=create_points_log.points_log_form.cleaned_data["points_log_class"],
                points_log_type=create_points_log.points_log_form.cleaned_data["points_log_type"],
                points_log_amount=create_points_log.points_log_form.cleaned_data["points_log_amount"],
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
        create_points_log.points_log_form = PointsLogCreateEditForm()


@login_required
def index(request):
    all_classes = Classes.objects.all()

    create_classes(request)
    create_points_log(request)

    return render(request, "index.html", {
        "classes_form": create_classes.classes_form,
        "points_log_form": create_points_log.points_log_form,
        "classes": all_classes
    })


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

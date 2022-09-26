from django import forms
from .models import Classes, PointsLog, AddPointsLog, SubtractPointsLog
from django.core.validators import MinValueValidator, MaxValueValidator


class ClassesEditCreateForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = "__all__"


class PointsLogCreateEditForm(forms.Form):
    points_log_class = forms.ModelChoiceField(
        label="Class",
        queryset=Classes.objects.all(),
        error_messages={
            "required": "Please choose class for log",
        })
    points_log_type = forms.ChoiceField(
        label="Type",
        choices=PointsLog.POINTS_LOG_TYPE_CHOICES,
        error_messages={
            "required": "Please choose type of log."
        })
    points_log_amount = forms.IntegerField(
        label="Amount",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        error_messages={
            "required": "Please enter amount of points to add/subtract",
            "min_value": "Min add/subtract log amount - 1",
            "max_value": "Max add/subtract log amount - 100"
        })


class AddPointsLogCreateEditForm(forms.Form):
    points_add_log_amount = forms.IntegerField(
        label="Amount",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        error_messages={
            "required": "Please enter amount of points to add",
            "min_value": "Min add log amount - 1",
            "max_value": "Max add log amount - 100"
        })


class SubtractPointsLogCreateEditForm(forms.Form):
    points_subtract_log_amount = forms.IntegerField(
        label="Amount",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        error_messages={
            "required": "Please enter amount of points to subtract",
            "min_value": "Min subtract log amount - 1",
            "max_value": "Max subtract log amount - 100"
        })

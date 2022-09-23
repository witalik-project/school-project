from django import forms
from .models import Classes, PointsLog, AddPointsLog, SubtractPointsLog


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
        error_messages={
            "required": "Please enter amount of points to add/subtract",
            "max_length": "Please enter valid amount"
        })


class AddPointsLogCreateEditForm(forms.Form):
    points_add_log_amount = forms.IntegerField(
        label="Amount",
        error_messages={
            "required": "Please enter amount of points to add",
            "max_length": "Please enter valid amount"
        })


class SubtractPointsLogCreateEditForm(forms.Form):
    points_subtract_log_amount = forms.IntegerField(
        label="Amount",
        error_messages={
            "required": "Please enter amount of points to subtract",
            "max_length": "Please enter valid amount"
        })

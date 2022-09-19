from django import forms
from .models import Classes, PointsLog


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

from django import forms
from .models import Classes, PointsLog
from django.core.validators import MinValueValidator, MaxValueValidator


class ClassesEditCreateForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = "__all__"


class ClassesEditExceptPointsForm(forms.ModelForm):

    class Meta:
        model = Classes
        exclude = ("class_points",)


class PointsLogCreateEditForm(forms.Form):
    points_log_class = forms.ModelChoiceField(
        label="Class",
        queryset=Classes.objects.all(),
        error_messages={
            "required": "Please choose class for log",
        })
    points_log_type = forms.BooleanField(
        label="Check if you want to ADD",
        required=False
        )
    points_log_amount = forms.IntegerField(
        label="Amount",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        error_messages={
            "required": "Please enter amount of points to add/subtract",
            "min_value": "Min add/subtract log amount - 1",
            "max_value": "Max add/subtract log amount - 100"
        })
    points_log_description = forms.CharField(
        widget=forms.Textarea,
        required=False
    )


class PointsAddSubtractLogCreateEditForm(forms.Form):
    points_log_amount = forms.IntegerField(
        label="Amount",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        error_messages={
            "required": "Please enter amount of points to add/subtract",
            "min_value": "Min add/subtract log amount - 1",
            "max_value": "Max add/subtract log amount - 100"
        })
    points_log_description = forms.CharField(
        widget=forms.Textarea,
        required=False
    )



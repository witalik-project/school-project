from django import forms
from .models import Classes, PointsLog
from django.core.validators import MinValueValidator, MaxValueValidator


class ClassesEditCreateForm(forms.Form):
    SCHOOL_LETTER_CHOICES = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
    ]
    SCHOOL_LEVEL_CHOICES = [
        ("Primary school", "Primary school"),
        ("Secondary school", "Secondary school"),
        ("High school", "High school")
    ]

    class_number = forms.IntegerField(
        label="Class number",
    )
    class_letter = forms.ChoiceField(
        label="Class letter",
        choices=SCHOOL_LETTER_CHOICES
    )
    class_school_level = forms.ChoiceField(
        label="Class school level",
        choices=SCHOOL_LEVEL_CHOICES
    )
    class_teacher_name = forms.CharField(
        label="Class teacher name",
    )
    class_teacher_surname = forms.CharField(
        label="Class teacher surname",
    )
    class_points = forms.IntegerField(
        label="Class points",
        validators=[MinValueValidator(0), MaxValueValidator(999)],
    )
    class_photo = forms.ImageField(
        label="Class photo",
        required=False
    )


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

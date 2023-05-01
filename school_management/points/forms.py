from django import forms
from .models import Classes, PointsLog
from django.core.validators import MinValueValidator, MaxValueValidator


class ClassesCreateEditForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = "__all__"


# TODO: NOT USING
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
        error_messages={
            "required": "Please provide class number"
        }
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


class ClassesEditExceptPointsForm(forms.ModelForm):
    class Meta:
        model = Classes
        exclude = ("class_points",)


class PointsLogCreateForm(forms.Form):
    CHOICES = (
        (True, 'Dodać'),
        (None, 'Odjąć')
    )

    points_log_class = forms.ModelChoiceField(
        label="Klasa rejestru",
        queryset=Classes.objects.all(),
    )
    points_log_type = forms.ChoiceField(
        label="Dodać lub odjąć punkty",
        choices=CHOICES,
        required=False,
        initial='Dodać'
    )
    points_log_amount = forms.IntegerField(
        label="Ilość",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        error_messages={
            "required": "Proszę podać ilość punktów by dodać/odjąć",
            "min_value": "Minimalna ilość punktów by dodać/odjąć - 1",
            "max_value": "Maksymalna ilość punktów by dodać/odjąć - 100"
        })
    points_log_description = forms.CharField(
        label="Opis",
        widget=forms.Textarea,
        required=False
    )


class PointsAddSubtractLogCreateEditForm(forms.Form):
    points_log_amount = forms.IntegerField(
        label="Ilość",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        error_messages={
            "required": "Proszę podać ilość punktów by dodać/odjąć",
            "min_value": "Minimalna ilość punktów by dodać/odjąć - 1",
            "max_value": "Maksymalna ilość punktów by dodać/odjąć - 100"
        })
    points_log_description = forms.CharField(
        label="Opis",
        widget=forms.Textarea,
        required=False
    )

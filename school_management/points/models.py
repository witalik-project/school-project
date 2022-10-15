from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.utils import timezone


class Classes(models.Model):
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

    class_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], null=False)
    class_letter = models.CharField(max_length=1, choices=SCHOOL_LETTER_CHOICES, default="A")
    class_school_level = models.CharField(max_length=16, choices=SCHOOL_LEVEL_CHOICES, default="Primary school")
    class_teacher_name = models.CharField(max_length=20)
    class_teacher_surname = models.CharField(max_length=20)
    class_points = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)], null=False)
    class_photo = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return f"{self.class_number}{str(self.class_letter).capitalize()} - {self.class_school_level}"


class PointsLog(models.Model):
    points_log_class = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    points_log_date = models.DateTimeField(auto_now_add=True)
    points_log_type = models.BooleanField(blank=True, null=True)
    points_log_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], null=False)
    points_log_description = models.TextField(blank=True, null=True, help_text="Write some description if you need.")
    points_log_created_by = models.CharField(max_length=30, null=True)

    def __str__(self):
        if self.points_log_type:
            return f"{self.points_log_class} - {self.points_log_date} - ADDED {self.points_log_amount} points."
        else:
            return f"{self.points_log_class} - {self.points_log_date} - SUBTRACTED {self.points_log_amount} points."

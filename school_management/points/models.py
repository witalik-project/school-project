from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    class_photo = models.ImageField(upload_to="images", default="./uploads/images/default.jpg", null=True)

    def __str__(self):
        return f"{self.class_number}{str(self.class_letter).capitalize()} - {self.class_school_level}"


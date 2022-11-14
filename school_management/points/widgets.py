from django import forms


class DatePickerWidget(forms.DateInput):
    input_type = "date"

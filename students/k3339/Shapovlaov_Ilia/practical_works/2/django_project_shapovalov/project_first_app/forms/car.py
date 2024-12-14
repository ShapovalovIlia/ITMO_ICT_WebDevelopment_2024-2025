from django import forms  # type: ignore
from project_first_app.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["state_number", "brand", "model", "colour"]

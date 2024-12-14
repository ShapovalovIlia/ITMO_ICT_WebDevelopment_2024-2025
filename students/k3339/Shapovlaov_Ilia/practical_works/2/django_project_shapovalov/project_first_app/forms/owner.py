from django import forms  # type: ignore
from project_first_app.models import Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ["surname", "name", "date_of_birth"]

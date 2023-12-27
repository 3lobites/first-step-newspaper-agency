from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from newspaper_agency.models import Redactor, Newspaper


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search redactor"
            }
        )
    )


class RedactorDataUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ["last_name", "first_name", "years_of_experience"]
    pass


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = "__all__"

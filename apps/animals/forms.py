from django import forms

from apps.animals.models import Animal


class GenerateForm(forms.Form):
    amount = forms.IntegerField(
        label="Amount",
        min_value=1,
        max_value=100,
        required=True,
        initial=10,
    )


class AnimalSpecialEditForm(forms.ModelForm):
    class Meta:
        model = Animal

        fields = (
            "name",
            "age",
            "is_auto_generated",
        )

from django import forms

from nested_form_field import NestedFormField

from .models import Record


class NestedNestedForm(forms.Form):
    age = forms.IntegerField(min_value=18)


class NestedForm(forms.Form):
    name = forms.CharField()
    nested_form = NestedFormField(form_class=NestedNestedForm)


class ExampleForm(forms.ModelForm):
    nested_form = NestedFormField(form_class=NestedForm)

    class Meta:
        model = Record
        fields = ["nested_form"]

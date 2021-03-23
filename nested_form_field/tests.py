from django import forms
from django.test import TestCase

from nested_form_field import NestedFormField


class TestSimpleNestedForm(TestCase):
    def test(self):
        class BookForm(forms.Form):
            title = forms.CharField()

        class SimpleForm(forms.Form):
            book = NestedFormField(BookForm)

        data = {"book_title": "Moby Dick"}
        form = SimpleForm(data=data)
        assert form.is_valid(), form.errors.as_text()
        assert form.clean() == {"book": {"title": "Moby Dick"}}, form.cleaned_data

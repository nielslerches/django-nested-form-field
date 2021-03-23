from collections import Mapping
from typing import Type

from django import forms


class NestedFormField(forms.MultiValueField):
    def __init__(self, form_class: Type[forms.Form], *args, **kwargs):
        self.form_class: Type[forms.Form] = form_class
        super().__init__(
            fields=tuple(self.form_class().fields.values()),
            widget=NestedFormWidget(form_class=form_class),
            *args,
            **kwargs
        )

    def compress(self, data_list):
        return {
            key: data_list[i] for i, key in enumerate(self.form_class().fields.keys())
        }


class NestedFormWidget(forms.MultiWidget):
    template_name = "nested_form_field/widgets/nested_form.html"

    def __init__(self, form_class: Type[forms.Form], *args, **kwargs):
        self.form_class: Type[forms.Form] = form_class
        super().__init__(
            widgets={
                name: boundfield.widget
                for name, boundfield in self.form_class().fields.items()
            },
            *args,
            **kwargs
        )

    def decompress(self, value):
        if isinstance(value, Mapping):
            return [value.get(name) for name in self.form_class().fields.keys()]
        return [None for _ in self.form_class().fields]

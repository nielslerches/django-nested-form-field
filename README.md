# django-nested-form-field

nest django forms as fields in other forms

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django-nested-form-field.

```bash
pip install django-nested-form-field
```

## Usage

```python
from django import forms

from nested_form_field import NestedFormField


class MyNestedForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()


class MyForm(forms.Form):
    nested_form = NestedFormField(MyNestedForm)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

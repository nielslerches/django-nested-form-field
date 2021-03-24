from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="django-nested-form-field",
    version="0.0.1",
    description="nest django forms as fields in other forms",
    license="MIT",
    long_description=long_description,
    author="Niels Lerche Sørensen",
    url="https://github.com/ebanalyse/django-nested-form-field",
    packages=["nested_form_field"],
    install_requires=["django>=3.1"],  # external packages as dependencies
)

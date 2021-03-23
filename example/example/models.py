from django.db import models


class Record(models.Model):
    nested_form = models.JSONField()

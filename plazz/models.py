from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=255)
    enabled = models.BooleanField()


class FieldType(models.Model):
    type = models.CharField(max_length=255)


class FormField(models.Model):
    index = models.IntegerField(default=0)
    label = models.CharField(max_length=255)
    required = models.BooleanField()
    form = models.ForeignKey(Form, unique=True, on_delete=models.CASCADE)
    fieldtype = models.ForeignKey(FieldType, on_delete=models.CASCADE)


class FieldOption(models.Model):
    index = models.IntegerField(primary_key=True)
    disabled = models.BooleanField()
    selected = models.BooleanField()
    value = models.CharField(max_length=255)
    formfield = models.ForeignKey(FormField, on_delete=models.CASCADE)

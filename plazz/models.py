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
    min = models.CharField(max_length=255, null=True)
    max = models.CharField(max_length=255, null=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    fieldtype = models.ForeignKey(FieldType, on_delete=models.CASCADE)


class FieldOption(models.Model):
    index = models.IntegerField(default=0)
    disabled = models.BooleanField()
    selected = models.BooleanField()
    value = models.CharField(max_length=255)
    formfield = models.ForeignKey(FormField, on_delete=models.CASCADE)


class Street(models.Model):
    name = models.CharField(max_length=255)


class State(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    name = models.CharField(max_length=255)
    Sec_edu = models.IntegerField(default=0)
    Sec_vocational_edu = models.IntegerField(default=0)
    Higher_prof_edu_bachelor = models.IntegerField(default=0)
    Wo_master_doctoraal = models.IntegerField(default=0)


class StateCity(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255, null=True)


class Location(models.Model):
    long = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    house_nr = models.CharField(max_length=10)
    postalcode = models.CharField(max_length=30)
    rent_month = models.DecimalField(decimal_places=2, max_digits=10)
    square_meter = models.IntegerField(default=0)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    state_city = models.ForeignKey(StateCity, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)


class NeighbourhoodCity(models.Model):
    Avg_restaurant_dist = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    Avg_restaurant_amt_1_km = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    Avg_restaurant_amt_3_km = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    Avg_restaurant_amt_5_km = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    Age_0_to_15 = models.IntegerField(default=0)
    Age_15_to_25 = models.IntegerField(default=0)
    Age_25_to_45 = models.IntegerField(default=0)
    Age_45_to_65 = models.IntegerField(default=0)
    Age_65_or_older = models.IntegerField(default=0)
    Avg_income = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    Population = models.IntegerField(default=0)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

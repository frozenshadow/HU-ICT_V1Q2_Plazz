from django.contrib import admin

from .models import Form, FieldType, FormField, FieldOption, NeighbourhoodCity, Neighbourhood, Location, StateCity, \
    Street, State, City

admin.site.register([
    Form,
    FieldType,
    FormField,
    FieldOption,
    Street,
    State,
    City,
    StateCity,
    Location,
    Neighbourhood,
    NeighbourhoodCity
])

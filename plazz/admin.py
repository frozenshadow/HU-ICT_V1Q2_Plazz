from django.contrib import admin

from .models import Form, FieldType, FormField, FieldOption

admin.site.register([Form, FieldType, FormField, FieldOption])

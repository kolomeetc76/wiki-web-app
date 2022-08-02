from django.contrib import admin
from django.forms import ModelForm
from .models import Task
from django_summernote.admin import SummernoteModelAdmin


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Task, SomeModelAdmin)


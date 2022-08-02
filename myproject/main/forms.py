from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Write name',
            }),
            "task": SummernoteWidget(attrs={
                'summernote': {
                    'airMode': False,
                    'width': '100%',
                    'height': '800',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['fontsize', ['fontsize']],
                        ['color', ['color']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['height', ['height']],
                        ['misc', ['codeview']],
                    ],

                },

            }),

        }




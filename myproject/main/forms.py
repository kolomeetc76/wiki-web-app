from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django_summernote.widgets import SummernoteWidget

#Форма создания записи(текстовый редактор, присвоение иерархии в дереве)
class add_TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "task", "parent"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Write name',
            }),

            "task": SummernoteWidget(attrs={
                'summernote': {
                    'airMode': False,
                    'width': '100%',
                    'height': '600',
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
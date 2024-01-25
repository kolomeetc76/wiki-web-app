from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Task

@registry.register_document
class YourModelDocument(Document):
    class Index:
        # Название индекса в Elasticsearch
        name = 'task-index'

    class Django:
        model = Task  # Модель, связанная с этим документом

        # Поля, которые вы хотите проиндексировать
        fields = [
            'name',
            'task'
        ]

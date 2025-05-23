from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField()
    description = models.CharField()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

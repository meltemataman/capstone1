from django.db import models

# Create your models here.
# Activity 2.01: Project ve Task modelleri
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Activity 3.01: Book modeli
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
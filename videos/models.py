from django.db import models

# Create your models here.
class video(models.Model):
    title = models.CharField(max_length=200)
    category = models.TextField(blank=True,null=True)
    author = models.CharField()
    duration = models.DurationField()
    time_uploaded = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    link = models.CharField(max_length=200)
    content = models.BinaryField()
    
    def __str__(self):
        return f"{self.title} by {self.author}"[:50] + "..."

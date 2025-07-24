from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} ({self.date})"


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')

    def __str__(self):
        return f"{self.name} - {self.event.title}"
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.date.date()})"


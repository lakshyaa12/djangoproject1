from django.db import models

class Contact(models.Model):  # Rename the model to Contact
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name

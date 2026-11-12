from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.full_name

class Employer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    employer_id = models.CharField(max_length=100)
    date_hired = models.DateField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} ({self.employer_id})"
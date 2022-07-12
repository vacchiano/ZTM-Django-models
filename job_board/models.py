from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=255)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.company} | Active: {self.is_active}"

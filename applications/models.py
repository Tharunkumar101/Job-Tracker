from django.db import models

class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('Applied','Applied'),
        ('Interview','Interview'),
        ('Offer','Offer'),
        ('Rejected','Rejected')
    ]

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    applied_date = models.DateField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.company
from django.db import models

# Create your models here.
class AddMembers(models.Model):
    firstname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    edu = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    town = models.CharField(max_length=100, blank=True)
    phone_home = models.IntegerField(null=True, blank=True)
    phone_cell = models.IntegerField(null=True, blank=True)
    first_liu = models.CharField(max_length=10, blank=True)
    applied_membership = models.CharField(max_length=20, blank=True)
    liu_id = models.CharField(max_length=10, blank=True)
    notes = models.TextField(blank=True)
    active_member = models.BooleanField()

    def __unicode__(self):
        return self.firstname + " " + self.surname

class LoadCSV(models.Model):
    def loadCSV(self, csv_file):
        return "asd"

from django.db import models

# Create your models here.
class SeeMembers(models.Model):
    def __unicode__(self):
        return self.firstname + " " + self.surname
    

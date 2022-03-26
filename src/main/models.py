from django.db import models

# Create your models here.
class Contact(models.Model):
   msg_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   phone = models.CharField(max_length=70)
   message = models.TextField()

   # def __str__(self):
   #    return self.name

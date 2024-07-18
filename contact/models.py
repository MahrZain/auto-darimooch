from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    
    def __str__(self):
        return 'Message From: ' +  self.name  + ' - ' + self.email

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact_Group(models.Model):

    type=models.CharField(max_length=250)
    
    class Meta:
        db_table="contact_group"
    
    def __str__(s):
        return s.type

    


class Contact(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20,default=" ")
    contact=models.BigIntegerField(default=1234567890)
    email=models.EmailField()
    address=models.CharField(max_length=255)
    category=models.ForeignKey(Contact_Group,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="contact"
    
    def showCategoryName(s):
        return s.category.type
    def showUserName(s):
        return s.user.username





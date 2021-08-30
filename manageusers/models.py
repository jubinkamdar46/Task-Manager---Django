from django.db import models

# Create your models here.
class Users(models.Model):
    user_email = models.CharField(max_length=100,unique=True)
    user_password = models.CharField(max_length=50)
    user_age = models.IntegerField()
    user_occupation = models.CharField(max_length=50)
    user_gender = models.CharField(max_length=10)
    user_state = models.CharField(max_length=50)
    user_zipcode =  models.IntegerField()
   
    # to change the object name to email of the user in admin panel
    def __str__(self):
       return self.user_email


class Tasks(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.CharField(max_length=250)
    task_duedate = models.DateField()
    task_priority = models.CharField(max_length=20)
    task_assignee = models.CharField(max_length=100)
    task_assignto = models.CharField(max_length=100)

    # to change the object name to email of the user in admin panel
    def __str__(self):
        return self.task_title



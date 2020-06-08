from django.db import models

# Create your models here.

class users(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    user_id = models.IntegerField()

    def __str__(self):
        return self.firstname

class matchmaking(models.Model):
    user_id = models.ManyToManyField('users')
    matchname = models.CharField(max_length=20)
    datetoplay = models.DateTimeField()
    city = models.CharField(max_length=20)
    price = models.IntegerField()
    match_id = models.IntegerField()

    def __str__(self):
        return self.matchname

class training(models.Model):
     
    user_id = models.ManyToManyField('users')
    form_name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    date = models.DateTimeField()
    training_id = models.IntegerField()

    def __str__(self):
        return self.form_name       


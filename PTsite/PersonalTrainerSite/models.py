from django.db import models
from django.contrib.auth.models import User


# Create your models here which are the blueprints of how we want to store out data

#TODO change up the customer field , because each login should have customers info in it. But get basics working for personal trainer first.
class Client(models.Model):

  #  userName = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)


    #returns the string representation of the object
    def __str__(self):
        return self.first_name + " " + self.last_name


class ClientGoals(models.Model):
    # allows the goals to be associated with the Customer.
    goals = models.ForeignKey(Client, on_delete=models.CASCADE)
    # TODO test and make sure when a client is deleted that it doesn't create unforeseen ripple effect <--

    # whenever a customer is deleted their associated data is deleted as well
    # customers weight goal

    current_weight = models.PositiveIntegerField(default=0)

    wight_goal = models.PositiveIntegerField(default=0)

    # customers photo if they choose to have one
    photo = models.ImageField(null=True)

# for now this are the admins for the website
class Trainer(models.Model):
    workout_name = models.CharField(max_length=30)

    # this fields holds an optional brief description of workout steps/process
    workout_desc = models.TextField(max_length=250)

    reps = models.PositiveIntegerField

    sets = models.PositiveIntegerField

# class Trainer(models.Model):
#     userName = models.ForeignKey('auth.User')
#     first_name = models.TextField(max_length=30)
#     last_name = model.TextField(max_length=30)
#     email = models.CharField(max_length=30)



from django.conf.urls import url
from . import views


# url pattern matches using those defined in the views.py file matched through regex
urlpatterns = [
    url(r'^$', views.mainPage, name='mainPage'),

    # once customers/clients have been added to the database use their primarykeys to redirect to the users personal page with their data goals and schedule
    url(r'^(?P<Customer>)/', views.clients, name='ClientsPage'),

    # first create a Trainer site that allows they to use

    url(r'^NewUser', views.createUser, name="CreateUser"),


    # this view is for Trainers to create their workout lists to later pull from for each customer by using checkboxes.
    # regular expression, view name/method , name of the method
    url(r'^CreateWorkouts', views.create_workouts, name='create_workouts'),

    # this is the url to display the users clients. TODO modify this to display current users primary key in the url, once has been implemented in model
    url(r'^MyClients', views.trainer_clients, name='trainer_clients'),

    url(r'^workoutList', views.workout_list, name='workout_list'),

    url(r'^new', views.post_new, name="post_new"),

    # uses the cusotomer id pk matching through their primary key number but i'm not there yet. TODO setup main page.
  #  url(r'^(?P<customer_id>[0-9]+)$', views.detail, name='ClientSite'),
]


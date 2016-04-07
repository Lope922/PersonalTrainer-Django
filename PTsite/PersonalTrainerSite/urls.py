from django.conf.urls import url
from . import views


# url pattern matches using those defined in the views.py file matched through regex
urlpatterns = [
    url(r'^$', views.mainPage, name='mainPage'),

    # once customers/clients have been added to the database use their primarykeys to redirect to the users personal page with their data goals and schedule
    url(r'^(?P<Customer>)/', views.clients, name='ClientsPage'),

    # first create a Trainer site that allows they to use

    url(r'^NewUser', views.createUser, name="CreateUser"),


    # this view is for Trainers to create thier workout lists to later pull from for each customer by using checkboxes.
    url(r'^CreateWorkouts', views.createWorkouts, name='createWorkouts')


    # uses the cusotomer id pk matching through their primary key number but i'm not there yet. TODO setup main page.
  #  url(r'^(?P<customer_id>[0-9]+)$', views.detail, name='ClientSite'),
]


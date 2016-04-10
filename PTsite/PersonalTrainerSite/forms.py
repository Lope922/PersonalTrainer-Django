from django.contrib.auth.models import User
from django import forms
from .models import Trainer


# this uses django's built in user functionality to build form based on define fields
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        # this needs to be implemented and tested.


class CreateWorkout(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = ("workout_name", "workout_desc", "reps", "sets")
# derived from stack overflow - stating my source
# http://stackoverflow.com/questions/11287485/taking-user-input-to-create-users-in-django

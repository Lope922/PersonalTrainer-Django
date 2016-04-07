from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        # this needs to be implemented and tested.

# derived from stack overflow - stating my source
# http://stackoverflow.com/questions/11287485/taking-user-input-to-create-users-in-django
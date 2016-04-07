from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .forms import UserForm , User

# this is just to get something working. This will later be a login page and then direct the user to the proper page. Either Trainer or customer.
# def index(request):
#     return HttpResponse("Hello , and welcome to the personal trainer website. Login to continue.")


#from here i am going to move onto the PersonalTriainerSite urls and setup the urls there.


#NOTES FROM THE NEW BOSTON WEBSITE

# returns user object if user credentials are correct
# user = authenticate(username=username, password= password)
#
#     if user is not None:
#         # make sure user account is not banned or deactivate
#         if user.is_active:
#             login(request, user)
#             #return redirect ('url.index')
#             # now to later call on this person by using
#             # request.user.username
#             # or requst.user.profilephoto or whatever
#     # if they are not authenticate or a user then return a different form.
#     return render(request, self.template_name, {'form':form})
def clients(request):
    return render(request, "pages/ClientsPage.html")

# recieves the html request and
def mainPage(request):
    return render(request, 'MainPage.html')
   # return HttpResponse("<h2>Details about Customer: " + str(Customer.first_name) + "</h2>")

def createUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            return HttpResponseRedirect('main.html')
    else:
        form = UserForm()
        # the third argument is a dictionary and it is optional. This returns the original form
    return render(request, 'CreateAccount.html', {'form': form})

def createWorkouts(request):
    return render(request, 'TrainerWorkoutList.html')
#    return render(request, 'CreateAccount.html')

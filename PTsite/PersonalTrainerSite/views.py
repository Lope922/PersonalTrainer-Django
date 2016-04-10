from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .forms import UserForm, User, CreateWorkout
from .models import Client

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


# receives the html request and
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

# after clicking the submit button if the method call the Post method. Check that input is valid. Then move onto ??? what page

#TODO get this working. Page is loading , but not adding items to the database.
def create_workouts(request):
    if request.method == "POST":
        # request the post method for the create workout form.
        form = CreateWorkout(request.POST)
        if form.is_valid():
            # used from blog demo
            # TODO rename this if it works
            post = form.save(commit=False)
            post.save()
            # redirect to the view name if input is valid
            return redirect(request, 'mainPage')
    else:
        form = CreateWorkout()
    return render(request, 'TrainerWorkoutList.html', {'form': form})
    # elif request.method == None:
    #     return HttpResponse("Nothing was returned for some reason" )
        # below is code from blog example that i can use when user  accounts are created with primary keys and diff
        # groups have been created as well
        # return redirect('post_detail', pk=post.pk)


#TODO  trying to use the new post template from the django girls blog to get the new workout added to the DATAbase
def post_new(request):
    form = CreateWorkout()
    return render(request, 'post_new', {'form': form})

# this is the page that displays the Trainers assigned clients that they have
def trainer_clients(request):
    c_1st_name = Client.fn

    c_last = Client.ln
    c_obj = Client.object.all()
    # try getting a list of all the clients within the database and displaying all of them for the current client.
    return render(request, 'TrainerClientPage.html', {'client': c_obj})

def workout_list(request):

    return render(request, '')

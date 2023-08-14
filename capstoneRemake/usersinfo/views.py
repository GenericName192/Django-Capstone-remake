from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserInfo, User
from django.forms import modelform_factory
from django.core.mail import send_mail

# team leads should not be able to change roles
userInfoFormTeamLead = modelform_factory(UserInfo, exclude=["role", "user"])
userInfoFormAdmin = modelform_factory(UserInfo, exclude=["user"])
# I am very unhappy with how this currently works but I could not think of a 
# way to accessing both forms without just hand writing the form, 
# if you are reading this and have a better way please contact me
userDetails = modelform_factory(User, exclude=["id", "password", "is_superuser", "username", "email", "is_staff", "date_joined", "last_login", "groups", "user_permissions", "is_active"])

# Create your views here.
def userRegister(request):
    if getUserRole(request.user.id) == "admin" or getUserRole(request.user.id) == "team lead":
        form = UserCreateForm()
        if request.method == "POST":
            form = UserCreateForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ("User created"))
                return redirect("home")
            
            else:
                return render(request, "./usersinfo/user-register.html", {"form": form})
        else:
            return render(request, "./usersinfo/user-register.html", {"form": form})
    else:
        messages.success(request, ("only team leads and admins can recruit new members"))
        return redirect("home")

def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login successful"))
            return redirect("home")
        else:
            messages.success(request, ("Login failed"))
            return redirect("login")
    else:
        return render(request, "./usersinfo/login.html")

def logoutUser(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect("home")

def userDetail(request, id):
    role = getUserRole(request.user.id)
    userInfo = get_object_or_404(UserInfo, pk=id)
    return render(request, "usersinfo/user-detail.html", {"userInfo": userInfo,
                                                          "role": role})

# as I said above I am very unhappy with how this function works but dont know a better way.
def userUpdate(request, id):
    userInfo = get_object_or_404(UserInfo, pk=id)
    useraccount = get_object_or_404(User, pk=id)
    role = getUserRole(request.user.id)
    form1 = userDetails(request.POST or None, instance=useraccount)
    if request.user.id == id: # so you cannot change your own role to prevent admins demoting selves
        form2 = userInfoFormTeamLead(request.POST or None, instance=userInfo)
    elif role == "admin":
        form2 = userInfoFormAdmin(request.POST or None, instance=userInfo)
    else:
        form2 = userInfoFormTeamLead(request.POST or None, instance=userInfo)
    if form1.is_valid():
        if form2.is_valid():
            form1.save()
            form2.save()
            return redirect("home")
    return render(request, "usersinfo/user-edit.html", {"userInfo": userInfo, 
                                                        "form1": form1,
                                                        "form2": form2,
                                                        "role": role,})


def userDelete(request, id):
    role = getUserRole(request.user.id)
    userInfo = get_object_or_404(UserInfo, pk=id)
    userAcount = get_object_or_404(User, pk=id)
    if getUserRole(request.user.id) == "admin":
        if request.method == "POST":
            userInfo.delete()
            userAcount.delete()
            return redirect("home")
    return render(request, "usersinfo/user-delete.html", {"userInfo": userInfo,
                                                          "role" : role})


def userPing(request, id):
    user = get_object_or_404(User, pk=id)
    emailTo = user.email
    send_mail(
        "ping", # subject
        "You have been pinged", #the email
        "", #  From email
        [emailTo] # To email
    )
    messages.success(request, ("Ping sent"))
    return redirect("home")


def getUserRole(userId):
    userRole = get_object_or_404(UserInfo, pk=userId).role
    return userRole


# shortcuts
from django.shortcuts import render

# tables
from usersinfo.models import Team, User

# query
from django.db.models import Q

#pagination
from django.core.paginator import Paginator


def isValidQueryparam(param):
    """ checks to see if there is something inside param aka what the user 
    is searching"""
    return param != '' and param is not None


# Create your views here.
def homepage(request):

        pUserInfo = Paginator(User.objects.all().order_by("first_name"), 5) # adds pagination to members
        Upage = request.GET.get("mPage") 
        userInfos = pUserInfo.get_page(Upage)
        pTeams = Paginator(Team.objects.all().order_by("name"), 5) # 2 pages so they wont affect each other
        Tpage = request.GET.get("tPage")
        teams = pTeams.get_page(Tpage)

        return render(request, "home/homepage.html", {
            "userInfos": userInfos,
            "teams": teams
        })

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
        
        # creates a list of all users and then filters them by whatever is in the search bar
        userList = User.objects.all().order_by("first_name")
        userContainsQuery = request.GET.get('searchUser')
        if isValidQueryparam(userContainsQuery):
            userList = userList.filter(Q(first_name__icontains=userContainsQuery)
                       | Q(last_name__icontains=userContainsQuery)
                       ).distinct()

        # creates a list of all teams and then filters them by whatever is in the search bar
        teamList = Team.objects.all().order_by("name")
        teamsContainsQuery = request.GET.get('searchTeam')
        if isValidQueryparam(teamsContainsQuery):
            teamList = teamList.filter(name__icontains=teamsContainsQuery)

        pUserInfo = Paginator(userList, 5) # adds pagination to members
        Upage = request.GET.get("mPage") 
        userInfos = pUserInfo.get_page(Upage)
        pTeams = Paginator(teamList, 5) # 2 pages so they wont affect each other
        Tpage = request.GET.get("tPage")
        teams = pTeams.get_page(Tpage)

        return render(request, "home/homepage.html", {
            "userInfos": userInfos,
            "teams": teams
        })

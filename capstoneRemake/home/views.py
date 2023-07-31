# shortcuts
from django.shortcuts import render

# tables
from usersinfo.models import UserInfo, Team


#pagination
from django.core.paginator import Paginator

# Create your views here.
def homepage(request):
        pUserInfo = Paginator(UserInfo.objects.all(), 5) # adds pagination to members
        pTeams = Paginator(Team.objects.all(), 5)
        Upage = request.GET.get("mPage") # 2 pages so they wont affect each other
        Tpage = request.GET.get("tPage")
        userInfos = pUserInfo.get_page(Upage)
        teams = pTeams.get_page(Tpage)

        return render(request, "home/homepage.html", {
            "userInfos": userInfos,
            "teams": teams
        })

# shortcuts
from django.shortcuts import redirect, render, get_object_or_404

# tables
from .models import Location
from teams.models import Team

# forms
from django.forms import modelform_factory

#pagination
from django.core.paginator import Paginator

from usersinfo.views import getUserRole

# query
from home.views import isValidQueryparam


def locations(request): # view all locations (may have to have this twice)

    p = Paginator( Location.objects.all().order_by("name"), 5)
    page = request.GET.get("page")
    locations = p.get_page(page)
    return render(request, "location/locations.html", {"locations": locations})


LocationForm = modelform_factory(Location, exclude=[])

def locationCreate(request):
    role = getUserRole(request.user.id)
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("locations")
    else:
        form = LocationForm()
    return render(request, "location/location-create.html", {"form": form,
                                                            "role": role})

def locationDetail(request, id): # select_related might be better here.
    role = getUserRole(request.user.id)
    location = get_object_or_404(Location, pk=id)
    teams = Team.objects.filter(location_id = id)
    return render(request, "location/location-detail.html", {"location": location,
                                                            "teams": teams,
                                                            "role": role})


def locationUpdate(request, id):
    role = getUserRole(request.user.id)
    location = get_object_or_404(Location, pk=id)
    form = LocationForm(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "location/location-update.html", {"location": location, 
                                                            "form": form,
                                                            "role": role})

def locationDelete(request, id):
    role = getUserRole(request.user.id)
    location = get_object_or_404(Location, pk=id)
    if request.method == "POST":
        location.delete()
        return redirect("home")
    return render(request, "location/location-delete.html", {"location": location,
                                                            "role": role})
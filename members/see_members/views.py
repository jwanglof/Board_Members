from django.shortcuts import render_to_response
from django.http import Http404
from add_members.models import AddMembers

def home(request):
    return render_to_response("home.html", {
        "members" : AddMembers.objects.all().order_by("surname")
    })

def member_specific(request, member_id):
    try:
        m = AddMembers.objects.get(pk=member_id)
    except:
        raise Http404

    return render_to_response("member_specific.html", {
        "member" : m
    })

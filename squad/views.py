from django.shortcuts import render
from squad.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


def overview(request):
    ranks = Group.objects.all()
    members = Member.objects.all()

    return render(request, 'squad_overview.html', {'ranks': ranks, 'members': members})


def retxml(request, user):
    try:
        member = Member.objects.get(nickname=user)
        return render(request, 'squad.xml', {'member': member})
    except ObjectDoesNotExist:
        return HttpResponse(None)

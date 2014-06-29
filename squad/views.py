from django.shortcuts import render
from squad.models import *


def overview(request):
    ranks = Group.objects.all()
    members = Member.objects.all()

    return render(request, 'squad_overview.html', {'ranks': ranks, 'members': members})


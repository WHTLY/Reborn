from django.shortcuts import render
from squad.models import Group, Member
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.http import HttpResponse
import os


def overview(request):
    ranks = Group.objects.all()
    members = Member.objects.all()

    return render(
        request,
        'squad_overview.html',
        {'ranks': ranks, 'members': members},
    )


def retxml(request, user):
    try:
        member = Member.objects.get(nickname=user)
        return render(request, 'squad.xml', {'member': member})
    except ObjectDoesNotExist:
        return HttpResponse(status=404)


def retlogo(request):
    """Return the squad logo as a binary stream."""
    logo_path = os.path.join(settings.STATIC_ROOT, 'slogo.paa')
    with open(logo_path, 'rb') as f:
        data = f.read()
    return HttpResponse(data, content_type='application/octet-stream')

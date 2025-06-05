from django.contrib import admin
from squad.models import Group, Member, Server, TimeStamp

admin.site.register(Member)
admin.site.register(Group)
admin.site.register(Server)
admin.site.register(TimeStamp)

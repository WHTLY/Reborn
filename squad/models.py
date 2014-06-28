from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    priority = models.IntegerField(default=50)

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=255)
    server_ip = models.IPAddressField()

    def __str__(self):
        return self.name


class Member(models.Model):
    nickname = models.CharField(max_length=50)
    aid = models.IntegerField(default=0)
    groups = models.ManyToManyField(Group)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nickname


class TimeStamp(models.Model):
    time = models.DateField(auto_now_add=True)
    server = models.ManyToManyField(Server)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return str(self.time)




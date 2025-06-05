from django.test import TestCase
from django.urls import reverse

from .models import Group, Server, Member


class ModelTests(TestCase):
    def test_group_str(self):
        group = Group.objects.create(name="Alpha", priority=1)
        self.assertEqual(str(group), "Alpha")

    def test_server_str(self):
        server = Server.objects.create(name="Main", server_ip="127.0.0.1")
        self.assertEqual(str(server), "Main")

    def test_member_str(self):
        group = Group.objects.create(name="Bravo", priority=10)
        member = Member.objects.create(nickname="User", aid=1)
        member.groups.add(group)
        self.assertEqual(str(member), "User")


class ViewTests(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name="Charlie", priority=5)
        self.member = Member.objects.create(nickname="Tester", aid=2)
        self.member.groups.add(self.group)

    def test_overview_view(self):
        response = self.client.get("/squad/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "squad_overview.html")

    def test_retxml_view(self):
        response = self.client.get(f"/squad/logo/{self.member.nickname}")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.member.nickname)

from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_index_get(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response=response, template_name='index.html')

    def test_scoreboard(self):
        response = self.client.get(reverse('scoreboard'))
        self.assertTemplateUsed(response=response, template_name='scoreboard.html')

# -*- coding: utf-8 -*-

from django.test import TestCase

from models import Shop, Good, Producer


class MainPageTest(TestCase):
    def setUp(self):
        self.producer1 = Producer.objects.create(name="Producer1")
        self.producer2 = Producer.objects.create(name="Producer2")

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

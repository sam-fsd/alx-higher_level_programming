#!/usr/bin/python3
"""
unit test for base class
"""

import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_Base_id_generation(self):
        b1 = Base()
        b2 = Base()

        self.assertEqual(b2.id, 2)

        b3 = Base(5)
        self.assertEqual(b3.id, 5)

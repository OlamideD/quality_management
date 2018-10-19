# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

test_dependencies = ["Quality Review"]

class TestQualityAction(unittest.TestCase):

	def test_quality_action(self):
		test_review, test_action = get_action()
		print(test_review.name, test_action.review)
		#self.assertEquals(test_review.name, test_action.review)

def get_action():
	review = frappe.get_list("Quality Review", fields=["name"])
	action = frappe.get_list("Quality Action", fields=["name" ,"review"])
	return review[0], action[0]
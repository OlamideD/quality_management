# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

test_dependencies = ["Quality Procedure", "Quality Goal", "Quality Review"]

class TestQualityAction(unittest.TestCase):

	def test_quality_action(self):
		test_review, test_action, test_procedure = get_action()
		print(test_review.name, test_action.review, test_procedure.name)
	#	self.assertEquals(test_review.name, test_action.review)

def get_action():
	review = frappe.get_list("Quality Review", fields=["name"])
	action = frappe.get_list("Quality Action", fields=["name" ,"review"])
	procedure = frappe.get_list("Quality Procedure", fields=["name"])
	return review[0], action[0], procedure[0]
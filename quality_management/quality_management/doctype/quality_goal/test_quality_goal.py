# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityGoal(unittest.TestCase):
	pass

#	def unit_test(self):
#		test_create_goal = create_goal()
#		test_get_goal = get_goal()
#		self.assertEquals(test_create_goal.name, test_get_goal.name)

#def create_goal():
#	goal = frappe.get_doc({
#		"doctype": "Quality Goal",
#		"goal": "Quality Goal Test",
#		"revision": "1",
#		"frequency": "Daily",
#		"objective": [
#			{
#				"objective": "Test Quality Goal 4",
#				"target": "4",
#			}
#		]
#	})
#	goal.insert()
#	return goal

#def get_goal():
#	goal = frappe.get_list("Quality Goal")
#	return goal[0]